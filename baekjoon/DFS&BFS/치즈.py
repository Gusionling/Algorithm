import sys
from collections import deque

input = sys.stdin.readline

#세로, 가로 
N, M = map(int, input().split())
hours = 0

dx = [1,-1,0,0]
dy = [0,0,-1,1]

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))  # 수정: 리스트 두 번 감싸기 제거
    
def bfs():
    # 출발점을 (0,0)으로 한다.
    queue = deque([(0,0)])
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 1  # 시작점 방문 처리
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]  
        
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == -1:
                # 빈칸인 경우 -> queue에 넣기
                if board[ny][nx] == 0:
                    visited[ny][nx] = 1  
                    queue.append((ny, nx))
                    
                # 치즈인 경우 +1
                else:
                    board[ny][nx] += 1
            
def melting():
    global hours  
    
    is_clear = True
    
    for y in range(N):
        for x in range(M):
            if board[y][x] == 2:
                board[y][x] = 1
                is_clear = False
            elif board[y][x] >= 3:
                board[y][x] = 0
            elif board[y][x] == 1:
                is_clear = False
    
    hours += 1
    return is_clear

while True:
    bfs()
    
    is_clear = melting()  
    
    if is_clear:
        break 

print(hours)