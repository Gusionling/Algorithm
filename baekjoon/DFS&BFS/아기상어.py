import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

sea = [list(map(int,input().split())) for _ in range(N)]
time = 0
size = 2

def find_start(sea):
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                return (i,j)

# 위쪽, 왼쪽, 아래, 오른쪽 순
dx = [0,-1,0,1]
dy = [-1,0,1,0]
total_time = 0

def bfs(size, sy, sx, time):
    queue = deque([(sy,sx)])
    time_table = [[-1] * N for _ in range(N)]
    time_table[sy][sx] = time
    size = 2

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            # 범위내 
            if 0<= ny <N and 0<= nx <N and sea[ny][nx] <= size and time_table[ny][nx] < 0:
                
                time_table[ny][nx] = time_table[y][x] + 1
                # 먹을 수 있는지
                if sea[ny][nx] < size:
                    size += sea[ny][nx]
                    sea[ny][nx] = 0
                    total_time = bfs(size, ny, nx, time_table[ny][nx])
                    return
    
    return total_time

sy, sx = find_start(sea)
print(bfs(2,sy,sx,0))
