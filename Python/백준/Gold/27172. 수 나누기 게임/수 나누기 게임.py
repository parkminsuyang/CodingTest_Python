import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int,input().split()))
max=10**6
count=[0]*(max+1)
for num in card:
    count[num]=1

score=[0]*(max+1)

for i in range (1,max+1):
    if count[i]==0:
        continue
    for j in range (i*2,max+1,i):
        if count[j]:
            score[i]+=1
            score[j]-=1

for c in card:
    print(score[c],end=' ')