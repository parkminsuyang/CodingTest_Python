import sys
from collections import deque

input=sys.stdin.readline

A,B,C=map(int,input().split())
visited=[[False]*(B+1) for _ in range(A+1)]
ans=set()

def bfs():
    queue=deque()
    queue.append((0,0))

    while queue:
        a,b=queue.popleft()
        c=C-a-b
        now=[a,b,c]
        if visited[a][b]:
            continue
        else:
            visited[a][b]=True
            if a==0:
                ans.add(c)
            for cur,nxt in ((0,1),(0,2),(1,0),(1,2),(2,0),(2,1)):
                if now[cur]==0:
                    continue
                else:
                    nxt_=now[:]
                    move=min(now[cur],[A,B,C][nxt]-now[nxt]) # 지금 물 용량, 받을 컵의 남은 물 용량
                    nxt_[cur]-=move
                    nxt_[nxt]+=move
                    queue.append((nxt_[0],nxt_[1]))


bfs()

print(' '.join(map(str,sorted(ans))))
