import sys
from collections import deque

input=sys.stdin.readline

n,k=map(int,input().split())
num=1000001
dist=[int(1e9)]*num
cnt=[0]*num

q=deque()
q.append(n)
dist[n]=0
cnt[n]=1
dx = [-1, +1, 0]

while q:
    cur = q.popleft()
    dx[2]=cur
    for d in range(3):
        nxt=dx[d]+cur

        if 0 <= nxt < num:
            if dist[nxt]>dist[cur]+1:
                dist[nxt]=dist[cur]+1
                cnt[nxt]=cnt[cur]
                q.append(nxt)
            elif dist[nxt]==dist[cur]+1:
                cnt[nxt]+=cnt[cur]

print(dist[k])
print(cnt[k])
