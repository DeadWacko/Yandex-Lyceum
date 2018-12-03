col_1=int(input())
col_2=int(input())
col_3=int(input())
mn_1=set()
mn_2=set()
mn_3=set()
n = 0
for i in range(col_1+col_2+col_3):
    st = str(input())
    if st in mn_1:
        if st in mn_2:
            mn_3.add(st)
            mn_2.remove(st)
        else:
            mn_2.add(st)
    else:
        mn_1.add(st)

n = len(mn_2)

if n != 0:
    print(n)
else:
    print('NO')