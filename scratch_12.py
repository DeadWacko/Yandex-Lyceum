col_1=int(input())
col_2=int(input())
mn_1=set()
mn_2=set()
for i in range(col_1+col_2):
    st = str(input())
    if st in mn_1:
        mn_2.add(st)
    else:
        mn_1.add(st)

if len(mn_1 ^ mn_2) == 0:
    print('NO')
else:
    print(len(mn_1 ^ mn_2))