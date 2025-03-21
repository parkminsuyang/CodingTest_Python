n,m=map(int,input().split())
num=list(map(int,input().split(' ')))
num.sort( )
temp=0
tt=0
for i in num:
    for j in num:
        for k in num:
            temp=i+j+k
            if (i!=j)&(i!=k)&(k!=j):
                if temp<=m:
                    if (m-tt)>(m-temp):
                        tt=temp
print(tt)