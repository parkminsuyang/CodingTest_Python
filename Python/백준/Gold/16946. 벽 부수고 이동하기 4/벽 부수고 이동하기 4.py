import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int,input().strip().split())
graph=[list(map(int,input().strip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
wasd=[(1,0),(0,-1),(-1,0),(0,1)]
group_size=dict()
group_id=1

def bfs(i,j,gid):
    queue=deque([(i,j)])
    visited[i][j]=gid
    cnt=1

    while queue:
        cur=queue.popleft()
        for nxt in wasd:
            ni=cur[0]+nxt[0]
            nj=cur[1]+nxt[1]
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if graph[ni][nj]==1:
                continue
            if visited[ni][nj]>0:
                continue
            visited[ni][nj]=gid
            cnt+=1
            queue.append((ni,nj))
    group_size[gid]=cnt

for i in range(n):
    for j in range(m):
        if graph[i][j]==0 and visited[i][j]==0:
            bfs(i,j,group_id)
            group_id+=1

res=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            group_set=set()
            for nxt in wasd:
                ni=i+nxt[0]
                nj=j+nxt[1]
                if 0<=ni<n and 0<=nj<m:
                    gid=visited[ni][nj]
                    if gid>0:
                        group_set.add(gid)

            for gid in group_set:
                res[i][j]+=group_size[gid]
            res[i][j]+=1
            res[i][j]%=10

for row in res:
    print(''.join(map(str,row)))

