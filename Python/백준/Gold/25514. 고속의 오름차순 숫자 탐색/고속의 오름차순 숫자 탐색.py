import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
targets = [1, 2, 3, 4, 5, 6]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r, c, target):
    q = deque()
    visited = [[False]*5 for _ in range(5)]
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        cx, cy, dist = q.popleft()

        #걷기
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1:
                if not visited[nx][ny]:
                    if board[nx][ny] == target:
                        return (nx, ny, dist+1)
                    visited[nx][ny] = True
                    q.append((nx, ny, dist+1))

            #뛰기: -1 도달 직전, 밖 도달 직전, 7도달
            nx, ny = cx, cy
            while True:
                nx += dx[d]
                ny += dy[d]
                if not (0 <= nx < 5 and 0 <= ny < 5):  # 보드 밖 직전
                    nx-=dx[d]
                    ny-=dy[d]
                    if not visited[nx][ny]:
                        if board[nx][ny]==target:
                            return (nx, ny, dist+1)
                        visited[nx][ny]=True
                        q.append((nx,ny,dist+1))
                    break

                if board[nx][ny] == -1:  # 벽 직전
                    nx -= dx[d]
                    ny -= dy[d]
                    if not visited[nx][ny]:
                        if board[nx][ny] == target:
                            return (nx, ny, dist + 1)
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))
                    break

                if board[nx][ny] == 7:  # 7 도달
                    if not visited[nx][ny]:
                        if board[nx][ny] == target:
                            return (nx, ny, dist + 1)
                        visited[nx][ny] = True
                        q.append((nx, ny, dist + 1))
                    break

    return None


total_moves = 0
cur_r, cur_c = r, c

for target in targets:
    res = bfs(cur_r, cur_c, target)
    if res is None:
        print(-1)
        sys.exit(0)
    cur_r, cur_c, moves = res
    total_moves += moves

print(total_moves)