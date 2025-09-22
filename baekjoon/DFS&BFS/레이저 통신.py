import sys
from collections import deque

input = sys.stdin.readline

matrix = []
switch = []
INF = float('inf')

# 상, 하, 좌, 우
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

# matrix 초기화
W, H = map(int, input().split())
for i in range(H):
    array = list(input().strip())
    for j in range(W):
        if array[j] == 'C':
            switch.append((i, j))
            array[j] = '.'
    matrix.append(array)

def solve():
    # visited[r][c][d] = (r,c)에서 d방향으로 올 때의 최소 거울 개수
    visited = [[[INF for _ in range(4)] for _ in range(W)] for _ in range(H)]
    queue = deque()
    
    start_r, start_c = switch[0]
    end_r, end_c = switch[1]
    
    # 시작점에서 4방향으로 출발
    for d in range(4):
        visited[start_r][start_c][d] = 0
        queue.append((start_r, start_c, d))
    
    while queue:
        r, c, direction = queue.popleft()
        
        # 현재 방향으로 계속 직진
        nr, nc = r + dr[direction], c + dc[direction]
        if 0 <= nr < H and 0 <= nc < W and matrix[nr][nc] != '*':
            if visited[nr][nc][direction] > visited[r][c][direction]:
                visited[nr][nc][direction] = visited[r][c][direction]
                queue.appendleft((nr, nc, direction))  # 비용 0이므로 앞에 추가
        
        # 다른 방향으로 꺾기 (거울 추가)
        for new_d in range(4):
            if new_d != direction:
                if visited[r][c][new_d] > visited[r][c][direction] + 1:
                    visited[r][c][new_d] = visited[r][c][direction] + 1
                    queue.append((r, c, new_d))  # 비용 1이므로 뒤에 추가
    
    # 목표점에서 모든 방향 중 최솟값
    result = min(visited[end_r][end_c])
    return result

print(solve())