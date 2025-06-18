import sys

input=sys.stdin.readline
n,m=map(int,input().split())
def backtrack(start,s):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(start,n+1):
        backtrack(i,s+[i])

backtrack(1,[])