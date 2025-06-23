import sys
from functools import reduce

input = sys.stdin.readline
n = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

vi = [[] for _ in range(n)]
amount = [0] * n
visited = [False] * n
common_multi = 1

for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    g = gcd(p, q)
    p //= g
    q //= g
    vi[a].append((b, p, q))
    vi[b].append((a, q, p))
    common_multi *= (p * q) // gcd(p, q)

amount[0] = common_multi

def dfs(node):
    visited[node] = True
    for next_node, p, q in vi[node]:
        if not visited[next_node]:
            amount[next_node] = amount[node] * q // p
            dfs(next_node)

dfs(0)
g = reduce(gcd, amount)
print(*[x // g for x in amount])
