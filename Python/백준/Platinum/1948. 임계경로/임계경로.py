import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[]for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]
indegre=[0]*(n+1)
time=[0]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().strip().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))
    indegre[b]+=1

start,end=map(int,input().split())

queue=deque([start])

#해당 도로까지 가는 최장 시간 계산->문제의 만나는 시간 계산
while queue:
    cur=queue.popleft()
    for nxt,t in graph[cur]:
        indegre[nxt]-=1
        if time[nxt]<time[cur]+t:
            time[nxt]=time[cur]+t
        if indegre[nxt]==0:
            queue.append(nxt)

print(time[end])

#역방향으로 도로의 개수 세기
visited=[False]*(n+1)
cnt=0
queue=deque([end])
visited[end]=True

while queue:
    cur=queue.popleft()
    for pre, t in reverse_graph[cur]:
        if time[cur]==time[pre]+t:
            cnt+=1
            if not visited[pre]:
                visited[pre]=True
                queue.append(pre)

print(cnt)