import sys
input=sys.stdin.readline

n,m=map(int,input().split())
truth=list(map(int,input().split()))
truth=truth[1:]
parent=[i for i in range(n+1)]


def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    parent_a=find(a)
    parent_b=find(b)
    if parent_a!=parent_b:
        parent[parent_b]=parent_a

parties=[]

for _ in range(m):
    p=list(map(int,input().split()))
    party=p[1:]
    parties.append(party)

    for i in range(1,len(party)):
        union(party[0],party[i])

res=0
for party in parties:
    isTrue=False
    for person in party:
        for t in truth:
            if find(t)==find(person):
                isTrue=True
                break
    if isTrue==False:
        res+=1
print(res)