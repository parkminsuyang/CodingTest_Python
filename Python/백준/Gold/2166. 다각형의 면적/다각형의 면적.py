#신발끈 공식

import sys
input=sys.stdin.readline

n=int(input())
dohyang=[]
sum=0

for _ in range(n):
    a,b=map(int,input().split())
    dohyang.append((a,b))
dohyang.append(dohyang[0])


for i in range(1,n+1):
    sum+=dohyang[i-1][0]*dohyang[i][1]-dohyang[i][0]*dohyang[i-1][1]
res=abs(sum)/2
print(round(res,1))