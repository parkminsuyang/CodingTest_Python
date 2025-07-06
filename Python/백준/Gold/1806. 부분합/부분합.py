import sys
input=sys.stdin.readline

n,s=map(int,input().split())
num=list(map(int,input().split()))


start,end,total,temp=0,0,num[0],1
res=int(1e9)

while True:
    if total>=s:
        res=min(temp,res)
        total-=num[start]
        start+=1
        temp-=1

    elif end==n-1:
        break

    else:
        end+=1
        temp+=1
        total+=num[end]


if res==int(1e9):
    print(0)
else:
    print(res)