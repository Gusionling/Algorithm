import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []

def bfs(x , y, grid):
    queue = deque([(x,y)])
    sum = 1
    grid[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if  0<=nx <M and 0<=ny<N  and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                sum += 1
                queue.append((nx, ny))
    result.append(sum)


M, N, K = map(int, input().split())

# 2차원 배열
grid = [[0] * N for _ in range(M)]

# 직사각형 영역 채우기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            grid[y][x] = 1


for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            bfs(i,j,grid)

# 결과 출력
result.sort()
print(len(result))
print(" ".join(map(str, result)))
