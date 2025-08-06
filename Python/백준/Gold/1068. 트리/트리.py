import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
graph=[[]for _ in range(n)]
temp=list(map(int,input().split()))
delete=int(input())
root=-1
for i in range(n):
    if temp[i]==-1:
        root=i
        continue
    graph[temp[i]].append(i)

def dfs(node):
    if node==delete:
        return 0
    if not graph[node]:
        return 1

    cnt=0
    for child in graph[node]:
        cnt+=dfs(child)
    if cnt==0:
        return 1
    return cnt

if root==delete:
    print(0)
else:
    print(dfs(root))