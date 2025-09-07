import sys
from collections import deque

input=sys.stdin.readline

#0은 빈 칸 1은 벽 2는 바이러스 | 벽은 3개 세우기
n,m=map(int,input().split())
world=[]
for _ in range(n):
    world.append(list(map(int,input().strip().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

max_safe=0

def bfs(lab): #안전구역 계산용
    global max_safe
    world=[row[:] for row in lab]
    q=deque()
    for i in range(n):
        for j in range(m):
            if world[i][j]==2:
                q.append((i,j))

    while q:
        cur=q.popleft()
        for d in range(4):
            nx,ny=cur[0]+dx[d],cur[1]+dy[d]
            if 0<=nx<n and 0<=ny<m:
                if world[nx][ny]==0:
                    world[nx][ny]=2
                    q.append((nx,ny))

    safe=sum(row.count(0) for row in world)
    max_safe=max(max_safe,safe)


def dfs(cnt):
    global max_safe
    if cnt==3:
        bfs(world)
        return
    for i in range(n):
        for j in range(m):
            if world[i][j]==0:
                world[i][j]=1
                dfs(cnt+1)
                world[i][j]=0

dfs(0)
print(max_safe)