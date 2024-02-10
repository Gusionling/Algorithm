from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(n)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([])
queue.append((0,0))

while queue:
        x, y = queue.popleft()
        # 상하 좌우 표시 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny <0 or ny >= m:
                continue
            # 처음 방문하는 경우에만 최단거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

print(miro[n-1][m-1])
