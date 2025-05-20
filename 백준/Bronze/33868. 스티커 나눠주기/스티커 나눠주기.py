n=int(input())

res=[]

for _ in range(n):
    res.append(list(map(int,input().split())))

T=res[0][0]
B=res[0][1]
for q,w in res[1:]:
    if q>T:
        T=q
    if w<B:
        B=w



a=T*B%7

print(a+1)