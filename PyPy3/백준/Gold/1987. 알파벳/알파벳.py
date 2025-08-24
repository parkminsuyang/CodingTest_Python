import sys

input = sys.stdin.readline

board=[]
r,c=map(int,input().split())
for _ in range(r):
    board.append(list(input().strip()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
visited=set()
max_len=0

def dfs(x,y,cnt):
    global max_len
    max_len=max(max_len,cnt)

    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<r and 0<=ny<c and board[nx][ny] not in visited:
            visited.add(board[nx][ny])
            dfs(nx,ny,cnt+1)
            visited.remove(board[nx][ny])

visited.add(board[0][0])
dfs(0,0,1)
print(max_len)



