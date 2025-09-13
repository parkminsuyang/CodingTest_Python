import sys

input=sys.stdin.readline

s1,s2,s3=map(int,input().split())
m=max(s1,s2,s3)
num=[0]*((m)*(m)+1)

for o in range(1,s1+1):
    for t in range(1,s2+1):
        for th in range(1,s3+1):
            num[o+t+th]+=1

large=0
idx=0
for i in range(1,len(num)):
    if num[i]>large:
        large=num[i]
        idx=i

print(idx)
