import sys
input=sys.stdin.readline

n=int(input())
liquid=list(map(int,input().split()))
liquid.sort()
temp=int(3e9)
res=[]
for i in range(n-2):
    start,end=i+1,n-1

    while start<end:
        total=liquid[i]+liquid[start]+liquid[end]

        if abs(total)<temp:
            temp=abs(total)
            res=[liquid[i],liquid[start],liquid[end]]
        if total<0:
           start+=1
        else:
            end-=1

print(*res)