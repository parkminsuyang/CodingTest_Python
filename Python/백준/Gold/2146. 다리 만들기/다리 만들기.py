
import sys
from collections import deque

input=sys.stdin.readline
n=int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS_1(a,b,num):
    queue=deque()
    queue.append((a,b))
    visited[a][b]=1
    graph[a][b] = num

    while queue:
        a,b=queue.popleft()
        for d in range(4):
            na,nb=a+dx[d],b+dy[d]
            if 0<=na<n and 0<=nb<n:
                if not visited[na][nb] and graph[na][nb]==1:
                    visited[na][nb]=1
                    graph[na][nb]=num
                    queue.append((na,nb))


#bfs1 활용 코드
num=2
for i in range(n):
    for j in range(n):
        if graph[i][j]==1 and not visited[i][j]:
            BFS_1(i,j,num)
            num+=1


def BFS_2():
    ans = int(1e9)
    for k in range(2,num):
        dist = [[-1] * n for _ in range(n)]
        queue=deque()

        for i in range(n):
            for j in range(n):
                if graph[i][j]==k:
                    queue.append((i,j))
                    dist[i][j]=0

        while queue:
            a,b=queue.popleft()
            for d in range(4):
                na,nb=a+dx[d],b+dy[d]
                if 0<=na<n and 0<=nb<n:
                    if graph[na][nb]==0 and dist[na][nb]==-1:
                        dist[na][nb]=dist[a][b]+1
                        queue.append((na,nb))
                    elif graph[na][nb] != 0 and graph[na][nb] != k:
                        ans=min(ans,dist[a][b])
                        break
    return ans
print(BFS_2())