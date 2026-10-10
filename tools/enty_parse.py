# -*- coding: utf-8 -*-
"""
enty_parse.py - Order of the Sinking Star .entities (enty) parser. v3

Format (reverse-engineered by static analysis of owned copy):

  Header:
    'enty' | u16 version(7) | u64 25 | u64 88 (type count)
    88 x [u64 len][ascii name][u64 attr_count]
    u32 instance_count
    prolog bytes (level dependent) then fd field stream.

  Field = fd | u8 id | u8 kind | payload

  kind 0x00:
    scalar  [u32 meta=0][f32]                 total 11
    string  [u64 0][u64 len][len ascii]       total 19+len
    ref     [u16 0x0890][u16 typ][u32 idx][6B pad][f32]  total 21  (payload starts 90 08)
    fd 0x0a [u64 0][u64 v]                    total 19  (v = 2/4 observed)
  kind 0x01..0x04: ref (same 21B shape)
  kind 0x10:
    int     [u32 0][i32 v]                    total 11  (when next byte is fd)
    int     [u64 0][i64 v]                    total 19
    string  [u64 0][u64 len][len ascii]       total 19+len
  fd 0x20:  [u64 0][u64 count][count x (u64 len + bytes)]  string array
            (empty strings = marker; non-empty = entity/asset names)
            FIRST field of each instance record.

  Instance record = [fd20 string-array (names)] [fields...] (next fd20 or EOF ends it)
  Common ids: 01-05 grid dims, 06-09 quat, 0a rot-extra/int, 0c tagged-int,
              16-18 bbox ext, 1a-1c bbox ctr, 1f editorUI string, 21/22/23 pos xyz,
              31 asset/mesh name string, 3b/db/92 refs.
"""
import struct, sys, os, json, glob
from collections import Counter

def is_ascii(b):
    return all(32 <= c < 127 for c in b)

class Reader:
    def __init__(self, data, off):
        self.d = data; self.p = off
    def u8(self):
        v = self.d[self.p]; self.p += 1; return v
    def u16(self):
        v = struct.unpack_from('<H', self.d, self.p)[0]; self.p += 2; return v
    def u32(self):
        v = struct.unpack_from('<I', self.d, self.p)[0]; self.p += 4; return v
    def u64(self):
        v = struct.unpack_from('<Q', self.d, self.p)[0]; self.p += 8; return v
    def bytes(self, k):
        v = self.d[self.p:self.p+k]; self.p += k; return v

def parse_fields(d, start, end):
    fields = []
    p = start
    while p + 3 <= end:
        if d[p] != 0xfd:
            p += 1
            continue
        fid, kind = d[p+1], d[p+2]
        # fd 0x20: string array [u64 0][u64 count][count x (u64 len + bytes)]
        # instance marker: usually empty strings; often holds entity/asset name
        if fid == 0x20 and kind == 0x00 and p + 19 <= end and \
           struct.unpack_from('<Q', d, p+3)[0] == 0:
            cnt = struct.unpack_from('<Q', d, p+11)[0]
            q = p + 19
            elems = []
            ok = 0 < cnt <= 4096
            while ok and len(elems) < cnt:
                if q + 8 > end:
                    ok = False; break
                ln = struct.unpack_from('<Q', d, q)[0]
                q += 8
                if ln > 512 or q + ln > end:
                    ok = False; break
                elems.append(d[q:q+ln])
                q += ln
            if ok and (q >= end or d[q] == 0xfd):
                strs = [e.decode('ascii') if is_ascii(e) else None for e in elems]
                fields.append(dict(off=p, id=fid, kind=kind, t='arr', v=strs))
                p = q
                continue
        # reference: payload = [u32 tag][u32 idx][6B zero pad][f32@+17] (21 total)
        # tag high16 = target type id (1..87), low16 = flag/version family (0x0890/0x0870/0x0650...)
        if p + 21 <= end and struct.unpack_from('<I', d, p+13)[0] == 0 and \
           (p + 21 >= end or d[p+21] == 0xfd):
            tag = struct.unpack_from('<I', d, p+3)[0]
            if ((d[p+3] == 0x90 and d[p+4] == 0x08) or kind in (1, 2, 3, 4)
                    or (1 <= (tag >> 16) <= 87 and (tag & 0xffff) >= 0x0100)):
                idx = struct.unpack_from('<I', d, p+7)[0]
                val = struct.unpack_from('<f', d, p+17)[0]
                fields.append(dict(off=p, id=fid, kind=kind, t='ref',
                                   v=dict(tag=tag, typ=tag >> 16, idx=idx, val=val)))
                p += 21
                continue
        if kind == 0x10 and p + 11 <= end:
            # string form
            if p + 19 <= end:
                ln = struct.unpack_from('<Q', d, p+11)[0]
                if 0 < ln <= 8192 and p+19+ln <= end and is_ascii(d[p+19:p+19+ln]):
                    fields.append(dict(off=p, id=fid, kind=kind, t='str',
                                       v=d[p+19:p+19+ln].decode('ascii')))
                    p = p + 19 + ln
                    continue
            # 8B small int [u32 0][i32]
            if struct.unpack_from('<I', d, p+3)[0] == 0:
                v = struct.unpack_from('<i', d, p+7)[0]
                fields.append(dict(off=p, id=fid, kind=kind, t='i', v=v))
                p += 11
                continue
            if p + 19 <= end:
                v = struct.unpack_from('<q', d, p+11)[0]
                fields.append(dict(off=p, id=fid, kind=kind, t='i', v=v))
                p += 19
                continue
        # fd 0x0a 19B integer form
        if fid == 0x0a and kind == 0x00 and p + 19 < end:
            hi = struct.unpack_from('<Q', d, p+11)[0]
            if hi != 0 and d[p+19] == 0xfd:
                fields.append(dict(off=p, id=fid, kind=kind, t='i', v=hi))
                p += 19
                continue
        # kind 0x00: tagged-int / string / scalar
        if kind == 0x00 and p + 11 <= end:
            meta0 = struct.unpack_from('<I', d, p+3)[0]
            raw0 = struct.unpack_from('<I', d, p+7)[0]
            if meta0 == 0 and (raw0 & 0xffff0000) == 0x08900000 and (raw0 & 0xffff):
                fields.append(dict(off=p, id=fid, kind=kind, t='tag',
                                   v=raw0 & 0xffff))
                p += 11
                continue
        if kind == 0x00 and p + 19 <= end:
            if struct.unpack_from('<Q', d, p+3)[0] == 0:
                ln = struct.unpack_from('<Q', d, p+11)[0]
                if 0 < ln <= 8192 and p+19+ln <= end and is_ascii(d[p+19:p+19+ln]):
                    fields.append(dict(off=p, id=fid, kind=kind, t='str',
                                       v=d[p+19:p+19+ln].decode('ascii')))
                    p = p + 19 + ln
                    continue
            # scalar [u32 meta][f32]
            meta = struct.unpack_from('<I', d, p+3)[0]
            val = struct.unpack_from('<f', d, p+7)[0]
            fields.append(dict(off=p, id=fid, kind=kind, t='f', v=val, meta=meta))
            p += 11
            continue
        fields.append(dict(off=p, id=fid, kind=kind, t='unk', v=None))
        p += 3
    return fields

def parse_enty(path):
    d = open(path, 'rb').read()
    if d[:4] != b'enty':
        raise ValueError('not enty')
    r = Reader(d, 4)
    ver = r.u16()
    a = r.u64(); ntypes = r.u64()
    names = []; attr_counts = []
    for _ in range(ntypes):
        ln = r.u64()
        names.append(r.bytes(ln).decode('ascii'))
        attr_counts.append(r.u64())
    n_inst = r.u32()
    fields = parse_fields(d, r.p, len(d))
    # Every fd 0x20 (array marker OR name string) starts a new instance block.
    bounds = [i for i, f in enumerate(fields)
              if f['id'] == 0x20 and f['t'] in ('arr', 'str')]
    insts = []
    for k, bi in enumerate(bounds):
        e = bounds[k+1] if k+1 < len(bounds) else len(fields)
        insts.append(fields[bi:e])
    pre = fields[:bounds[0]] if bounds else fields
    return dict(path=path, ver=ver, a=a, names=names, attr_counts=attr_counts,
                n_declared=n_inst, n_found=len(insts), fields=fields,
                insts=insts, preamble=pre)

# ---------------- per-instance semantic extraction ----------------

def fget(inst, fid):
    for f in inst:
        if f['id'] == fid and f['t'] in ('f', 'i', 'tag'):
            return f['v']
    return None

def extract(inst):
    o = {}
    p21, p22, p23 = fget(inst, 0x21), fget(inst, 0x22), fget(inst, 0x23)
    if p21 is not None or p22 is not None or p23 is not None:
        o['pos'] = [p21 if p21 is not None else 0.0,
                    p22 if p22 is not None else 0.0,
                    p23 if p23 is not None else 0.0]
    q = [fget(inst, x) for x in (0x06, 0x07, 0x08, 0x09)]
    if all(v is not None for v in q):
        o['rot'] = q
    ex = fget(inst, 0x0a)
    if ex is not None: o['rot_extra'] = ex
    dims = [fget(inst, x) for x in (0x01, 0x02, 0x03, 0x04, 0x05)]
    if not all(v is None for v in dims):
        o['dims'] = [0.0 if v is None else v for v in dims]
    ext = [fget(inst, x) for x in (0x16, 0x17, 0x18)]
    if not all(v is None for v in ext):
        o['bbox_ext'] = [0.0 if v is None else v for v in ext]
    ctr = [fget(inst, x) for x in (0x1a, 0x1b, 0x1c)]
    if not all(v is None for v in ctr):
        o['bbox_ctr'] = [0.0 if v is None else v for v in ctr]
    ui = next((f['v'] for f in inst if f['t'] == 'str' and f['id'] == 0x1f), None)
    if ui is not None: o['ui'] = ui
    refs = [dict(id=f['id'], **f['v']) for f in inst if f['t'] == 'ref']
    if refs: o['refs'] = refs
    ints = {f['id']: f['v'] for f in inst if f['t'] in ('i', 'tag')}
    if ints: o['ints'] = ints
    strs = [f['v'] for f in inst if f['t'] == 'str' and f['id'] != 0x1f]
    if strs: o['strs'] = strs
    arrs = [f['v'] for f in inst if f['t'] == 'arr' and len(f['v']) > 0]
    if arrs: o['arrs'] = arrs
    return o

# ---------------- batch ----------------

def main():
    lvl_dir = sys.argv[1] if len(sys.argv) > 1 else 'extract/levels/data-common'
    out_path = sys.argv[2] if len(sys.argv) > 2 else 'report/levels_layout.json'
    files = sorted(glob.glob(os.path.join(lvl_dir, '*.entities')))
    result = {}
    stats = dict(files=0, ok=0, mismatch=0, parse_err=0)
    unk_total = Counter()
    for fp in files:
        name = os.path.basename(fp)[:-len('.entities')]
        try:
            res = parse_enty(fp)
        except Exception as e:
            stats['parse_err'] += 1
            result[name] = dict(error=str(e))
            continue
        stats['files'] += 1
        ok = (res['n_declared'] == res['n_found'])
        stats['ok' if ok else 'mismatch'] += 1
        for f in res['fields']:
            if f['t'] == 'unk':
                unk_total[(f['id'], f['kind'])] += 1
        insts = [extract(i) for i in res['insts']]
        result[name] = dict(n_declared=res['n_declared'], n_found=res['n_found'],
                            instances=insts)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)
    print(json.dumps(stats))
    print('unk kinds:', dict(unk_total))
    for k in ('3d_intro_mirrors', 'ingame_glyphs', 'overworld'):
        if k in result and 'instances' in result[k]:
            r = result[k]
            withpos = sum(1 for i in r['instances'] if 'pos' in i)
            print('%s: decl=%s found=%s with_pos=%s' % (k, r['n_declared'], r['n_found'], withpos))

if __name__ == '__main__':
    main()
