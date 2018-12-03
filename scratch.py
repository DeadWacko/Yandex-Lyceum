bibl = int(input())
spis = int(input())
st = ''
mn_bibl = set()

for i in range(bibl):
    st = str(input())
    mn_bibl.add(st)
for i in range(spis):
    st = str(input())
    if st in mn_bibl:
        print('Yes')
    else:
        print('NO')