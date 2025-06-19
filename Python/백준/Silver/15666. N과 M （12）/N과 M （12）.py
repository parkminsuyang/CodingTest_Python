import sys

input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()

def backtrack(start,s):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    prev=-1
    for i in range(start,n):
        if num[i]!=prev:
            backtrack(i,s+num[i:i+1])
            prev=num[i]
backtrack(0,[])