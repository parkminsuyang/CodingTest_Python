import sys


input=sys.stdin.readline
n,m=map(int,input().split())
name=[]
nameIndex=dict()


for d in range(n):
    poket=input().strip()
    name.append(poket)
    nameIndex[poket]=d+1

for _ in range(m):
    q=input().strip()
    if q.isdigit():
        print(name[int(q)-1])
    else:
        print(nameIndex[q])