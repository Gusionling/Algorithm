import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

#목표지점 찾기
for i in range(n):
    for j in range(m):
        if array[i][j] == 2:
            dest = (j, i)
            break

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = map(int, q.popleft())
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx >=m or ny <0 or ny >= n or array[ny][nx] != 1:
                continue
            else:
                array[ny][nx] = array[y][x] + 1
                q.append((nx, ny))

bfs(dest[0], dest[1])

#배열 출력
for row in array:
    for item in row:
        if item == 0:
            print(0, end=' ')
        else:
            print(item-2, end=' ')
    print()


