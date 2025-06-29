import sys, heapq
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=[[]for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())

INF = int(1e9)
distance = [INF] * (n+1)

q = [(0,start)]
distance[start] = 0


while q:
    dist,now=heapq.heappop(q)

    if distance[now]<dist:
        continue

    for next_city,bus_cost in graph[now]:
        cost=dist+bus_cost

        if cost<distance[next_city]:
            distance[next_city] = cost
            heapq.heappush(q, (cost, next_city))
print(distance[end])