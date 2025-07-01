import sys
input=sys.stdin.readline
from collections import deque

n,k=map(int,input().split())

def bfs(n,k):
    visited=[-1]*100001
    queue=deque([n])
    visited[n]=0

    while queue:
        node=queue.popleft()
        if node==k:
            return visited[k]

        for next_node in (node*2,node-1,node+1):
            if 0<=next_node<=100000 :
                if visited[next_node]==-1:
                    if next_node==node*2:
                        visited[next_node]=visited[node]
                        queue.append(next_node)

                    else:
                        visited[next_node]=visited[node]+1
                        queue.append(next_node)

print(bfs(n,k))