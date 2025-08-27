import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#퀸 배치: 같은 행 같은 열 같은 대각선 X
n=int(input())
cnt=0

cols=[False]*n
leftright=[False]*(2*n)
rightleft=[False]*(2*n)

def dfs(x):
    global cnt

    for i in range(n):
        if cols[i]!=False or leftright[x+i]!=False or rightleft[(i-x)+n-1]!=False:
            continue
        else:
            cols[i]=leftright[x+i]=rightleft[(i-x)+n-1]=True
            if x==n-1:
                cnt+=1
            else:
                dfs(x+1)
            cols[i] = leftright[x + i] = rightleft[(i - x) + n-1] = False



dfs(0)
print(cnt)
