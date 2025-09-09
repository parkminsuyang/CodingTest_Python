import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
a.append(a[0])
cnt=0
for i in range(1,n+1):
    if a[i-1]>=a[i]:
        cnt+=1
print(cnt)