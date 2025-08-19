import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def steal(guid, keys, h, w):
    visited = [[False]*w for _ in range(h)]
    q = deque()

    # 문 위치 저장
    doors = {chr(i): [] for i in range(65, 91)}

    key = set()
    if keys[0] != '0':
        key.update(keys)

    # 외벽 초기화
    for i in range(h):
        for j in range(w):
            if i==0 or i==h-1 or j==0 or j==w-1:
                cell = guid[i][j]
                if cell == '*':
                    continue
                if 'A' <= cell <= 'Z' and cell.lower() not in key:
                    doors[cell].append((i,j))
                else:
                    q.append((i,j))
                    visited[i][j] = True


    res = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x, y = q.popleft()
        cell = guid[x][y]
        if cell == '$':
            res += 1
            guid[x][y] = '.'

        elif 'a' <= cell <= 'z':
            if cell not in key:
                key.add(cell)
                door_char = cell.upper()
                for door_x, door_y in doors[door_char]:
                    if not visited[door_x][door_y]:
                        q.append((door_x, door_y))
                        visited[door_x][door_y] = True
                        guid[door_x][door_y] = '.'
                doors[door_char] = []
            guid[x][y] = '.'

        elif 'A' <= cell <= 'Z':
            if cell.lower() in key:
                guid[x][y] = '.'
            else:
                doors[cell].append((x, y))
                continue

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<=nx<h and 0<=ny<w):
                continue
            if visited[nx][ny] or guid[nx][ny] == '*':
                continue

            nxt=guid[nx][ny]

            if 'A'<=nxt<='Z' and nxt.lower() not in key:
                doors[nxt].append((nx,ny))
                continue

            q.append((nx,ny))
            visited[nx][ny] = True

    print(res)

for _ in range(t):
    guid = []
    h, w = map(int, input().split())
    for _ in range(h):
        guid.append(list(input().strip()))
    keys = list(input().strip())
    steal(guid, keys, h, w)
