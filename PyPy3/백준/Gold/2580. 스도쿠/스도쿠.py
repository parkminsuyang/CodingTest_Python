import sys
input = sys.stdin.readline

board=[list(map(int,input().split())) for _ in range(9)]
zero=[]
for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            zero.append((i,j))

def check(x,y,n):
    #row
    if n in board[x]:
        return False
    #col
    for i in range(9):
        if board[i][y]==n:
            return False

    #3x3
    nx,ny=x//3,y//3

    for j in range(nx*3,(nx+1)*3):
        for k in range(ny*3,(ny+1)*3):
            if board[j][k]==n:
                return False
    return True

def dfs(idx):


    if idx==len(zero):
        for r in range(9):
            print(*board[r])
        exit()

    x,y=zero[idx][0],zero[idx][1]

    for i in range(1,10):
        if check(x,y,i):
            board[x][y]=i
            dfs(idx+1)
            board[x][y]=0

dfs(0)
