import sys

input=sys.stdin.readline

chess=[]
bchess=['BWBWBWBW','WBWBWBWB']*4
wchess=['WBWBWBWB','BWBWBWBW']*4
m,n=map(int,input().split())
for i in range(m):
    chess.append(input().strip())


Chess=[]
for i in range(0,m-7):
    for f in range(0, n - 7):
        bChess=0
        wChess=0
        for j in range(i,i+8):

            for k in range (f,f+8):
                if chess[j][k]!=bchess[j-i][k-f]:
                    bChess+=1
                if chess[j][k]!=wchess[j-i][k-f]:
                    wChess+=1
        Chess.append(min(bChess,wChess))

print(min(Chess))