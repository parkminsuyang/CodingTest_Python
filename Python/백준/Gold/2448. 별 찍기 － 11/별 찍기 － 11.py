import sys

input = sys.stdin.readline

n=int(input())
board=[[' ']*(2*n) for _ in range(n)]

def draw(x,y,size):
    if size==3:
        board[x][y]="*"
        board[x+1][y-1]=board[x+1][y+1]="*"
        board[x+2][y]="*"
        for i in range(1,3):
            board[x+2][y-i]=board[x+2][y+i]="*"
        return
    half=size//2
    draw(x,y,half)
    draw(x+half,y+half,half)
    draw(x+half,y-half,half)

draw(0,n-1,n)

for i in range(n):
    print("".join(board[i]))
