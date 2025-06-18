import sys

input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()

visited=[False]*n
def backtrack(s):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            backtrack(s+num[i:i+1])
            visited[i]=False

backtrack([])