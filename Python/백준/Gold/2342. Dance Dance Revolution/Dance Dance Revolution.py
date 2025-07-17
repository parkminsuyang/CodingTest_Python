import sys
input=sys.stdin.readline

todo=list(map(int,input().strip().split()))
todo.pop()
#dp[todo][왼발][오른발]
dp=[[[int(1e9)]*5 for _ in range(5)]for _ in range(len(todo)+1)]
dp[0][0][0]=0

def move_cost(cur,nxt):
    if cur==nxt:
        return 1
    elif cur==0:
        return 2
    elif cur-nxt==-2 or cur-nxt==2:
        return 4
    else:
        return 3

for to in range(len(todo)):
    move=todo[to]
    for left in range(5):
        for right in range(5):
            cost=dp[to][left][right]
            if cost==int(1e9):
                continue
            dp[to+1][move][right]=min(dp[to+1][move][right],cost+move_cost(left,move))
            dp[to+1][left][move]=min(dp[to+1][left][move],cost+move_cost(right,move))

res=int(1e9)
for i in range(5):
    for j in range(5):
        res=min(res,dp[len(todo)][i][j])
print(res)
