import sys
from itertools import combinations

input = sys.stdin.readline
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

home=[]
chicken=[]

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            home.append((i,j))
        elif board[i][j]==2:
            chicken.append((i,j))

def to_chicken(homex,homey,chickenx,chickeny):
    return abs(homex-chickenx)+abs(homey-chickeny)

remain_chicken=list(combinations(chicken,m))

res=int(1e9)
for chikens in remain_chicken:
    temp=0
    for hx,hy in home:
        len_chicken=int(1e9)
        for cx,cy in chikens:
            len_chicken=min(to_chicken(hx,hy,cx,cy),len_chicken)
        temp+=len_chicken
    res=min(temp, res)
print(res)