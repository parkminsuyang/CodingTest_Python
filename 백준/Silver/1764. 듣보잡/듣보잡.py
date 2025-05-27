import sys

input=sys.stdin.readline
n,m=map(int,input().split())
noListen=set([input().strip() for _ in range(n)])
noView=set([input().strip() for _ in range(m)])

noP=(noView&noListen)




print(len(noP))
print("\n".join(sorted(noP)))