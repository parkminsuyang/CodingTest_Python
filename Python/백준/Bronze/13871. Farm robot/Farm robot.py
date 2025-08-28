import sys
input=sys.stdin.readline

n,c,s=map(int,input().split())
to_go=list(map(int,input().split())) #시계

idx=0
res=0
if idx+1==s:
    res+=1
for t in to_go:

    if t==1:
        idx=(idx+1)%n
    else:
        idx=(idx-1)%n
    if idx+1==s:
        res+=1

print(res)