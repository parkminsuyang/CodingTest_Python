import sys
input=sys.stdin.readline

n=int(input())
trie={}

for _ in range(n):
    temp=list(input().split())
    k=int(temp[0])
    cur=trie
    for i in range(1,k+1):
        if temp[i] not in cur:
            cur[temp[i]]={}
        cur=cur[temp[i]]


def dfs(node,depth):
    for key in sorted(node.keys()):
        print('--'*depth+key)
        dfs(node[key],depth+1)

dfs(trie,0)