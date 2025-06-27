import sys
input=sys.stdin.readline

n=int(input())
tree=[[None,None] for _ in  range(26)]
for _ in range(n):
    a,b,c=input().split()
    idx=ord(a)-ord('A')
    if b=='.':
        tree[idx][0]=None
    else:
        tree[idx][0]=ord(b)-ord('A')
    if c=='.':
        tree[idx][1]=None
    else:
        tree[idx][1] = ord(c) - ord('A')


#전위 순회
def preorder(now):
    print(chr(now + ord('A')), end='')
    if tree[now][0] != None:
        preorder(tree[now][0])
    if tree[now][1] != None:
        preorder(tree[now][1])
preorder(0)
print('')
#중위 순회
def midorder(now):
    if tree[now][0] != None:
        midorder(tree[now][0])
    print(chr(now + ord('A')), end='')
    if tree[now][1] != None:
        midorder(tree[now][1])
midorder(0)
print('')
#후위 순회
def backorder(now):
    if tree[now][0] != None:
        backorder(tree[now][0])
    if tree[now][1] != None:
        backorder(tree[now][1])
    print(chr(now + ord('A')), end='')
backorder(0)