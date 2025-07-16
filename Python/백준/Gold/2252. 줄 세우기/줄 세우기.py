import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().split())
student=[[]for _ in range(n+1)]
snum=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    student[a].append(b)
    snum[b]+=1

res=[]
def bfs():
    queue=deque()

    for i in range(1,n+1):
        if snum[i]==0:
            queue.append(i)

    while queue:

        cur=queue.popleft()
        res.append(cur)
        for nxt in student[cur]:
            snum[nxt]-=1
            if snum[nxt]==0:
                queue.append(nxt)

bfs()
print(' '.join(map(str,res)) )
