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
    prev=-1
    for i in range(n):
        if visited[i]==False and num[i]!=prev:
            visited[i]=True
            backtrack(s+num[i:i+1])
            visited[i]=False
            prev=num[i]
backtrack([])