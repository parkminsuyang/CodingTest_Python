import sys
input=sys.stdin.readline

n=int(input())
baguette=[]
for _ in range(n):
    s,e=map(int,input().split())
    baguette.append((s,e))

baguette.sort(key=lambda  x:(x[0],-x[1]))
filtered_baguette=[]

for s,e in baguette:
    if filtered_baguette and filtered_baguette[-1][0]<=s and filtered_baguette[-1][1]>=e:
        continue
    filtered_baguette.append((s,e))

filtered_baguette.sort(key=lambda x:(x[1]))
cnt=0
last_cut=0


for s,e in filtered_baguette:
    if last_cut<=e:
        if last_cut>s:
            continue
        cnt+=1
        last_cut=e-1

print(cnt)