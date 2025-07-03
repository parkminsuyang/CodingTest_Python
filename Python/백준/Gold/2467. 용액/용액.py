import sys
input=sys.stdin.readline

n=int(input())
y=list(map(int,input().split()))
res=2000000001
left=0
right=n-1
a,b=0,0

while left<right:
    total=y[left]+y[right]

    if abs(total)<=res:
        res=abs(total)
        a,b=left,right
        if res==0:
            break

    if total<0:
        left+=1
    else:
        right-=1
print(y[a],y[b])