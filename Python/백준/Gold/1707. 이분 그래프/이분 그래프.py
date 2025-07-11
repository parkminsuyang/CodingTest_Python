import sys
from collections import deque

input=sys.stdin.readline

#테스트 케이스의 개수
k=int(input())

def check_graph(start,n):

    color=[0]*(n+1)


    for start in range(1,n+1):
        if color[start]!=0:
            continue

        queue=deque([start])
        color[start] = 1

        while queue:
            cur=queue.popleft()
            for nxt in graph[cur]:

                if color[nxt]==0:
                    color[nxt]=-color[cur]
                    queue.append(nxt)

                elif color[nxt]==color[cur]:
                    return 'NO'
    return 'YES'

for _ in range(k):

    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]

    for _ in range(e):
        U,V=map(int,input().split())
        graph[U].append(V)
        graph[V].append(U)

    print(check_graph(1,v))


