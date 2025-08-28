import sys
input=sys.stdin.readline

n,m=map(int,input().split())
ive=[]
distance=int(1e9)
res=[]

for _ in range(n):
    ive.append(list(map(int,input().split())))

for r in range(n):
    for c in range(m):
        if ive[r][c]==0:
            dis=(r+1)+abs((m+1)/2-(c+1))
            if dis<=distance:
                distance=dis
                res.append((r+1,c+1))

if res:
    print(*res.pop())
else:
    print(-1)