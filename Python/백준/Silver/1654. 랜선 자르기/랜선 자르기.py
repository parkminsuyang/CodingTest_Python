import sys
input=sys.stdin.readline
k,n=map(int,input().split())
lan=[]
for _ in range(k):
    lan.append(int(input()))

end=max(lan)
start=1
res=0
while start<=end:
    mid=((start+end)//2)
    total=0
    for i in range(k):
        total+=(lan[i]//mid)
    if total<n:
        end=mid-1
    else:
        res=mid
        start=mid+1
print(res)