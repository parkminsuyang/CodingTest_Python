import sys
from collections import deque

input=sys.stdin.readline


def bfs():
    queue = deque()

    for i in range(1, n + 1):
        if degree[i] == 0:
            queue.append(i)
            dp[i] = dime[i]

    while queue:
        cur = queue.popleft()
        for nxt in build[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + dime[nxt])
            degree[nxt] -= 1
            if degree[nxt] == 0:
                queue.append(nxt)


t=int(input())
for _ in range(t):
    n,k,=map(int,input().split())
    dime=list(map(int,input().strip().split()))
    dime.insert(0,0)
    build=[[] for _ in range(n+1)]
    degree=[0]*(n+1)
    dp=[0]*(n+1)
    for _ in range(k):
        x,y=map(int,input().split())
        build[x].append(y)
        degree[y]+=1

    w=int(input())
    bfs()
    print(dp[w])

