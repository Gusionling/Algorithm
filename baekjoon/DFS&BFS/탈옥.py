import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

T = int(input())
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs_01(start_points, jail, h, w):
    """0-1 BFS를 사용한 최단거리 계산"""
    visited = [[INF] * w for _ in range(h)]
    queue = deque()
    
    # 시작점들 초기화
    for r, c in start_points:
        if 0 <= r < h and 0 <= c < w and jail[r][c] != '*':
            visited[r][c] = 0
            queue.appendleft((r, c))
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < h and 0 <= nc < w and jail[nr][nc] != '*':
                cost = 1 if jail[nr][nc] == '#' else 0
                new_dist = visited[r][c] + cost
                
                if new_dist < visited[nr][nc]:
                    visited[nr][nc] = new_dist
                    if cost == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))
    
    return visited

for _ in range(T):
    h, w = map(int, input().split())
    prisoner = []
    
    # 보드 입력 받기    
    jail = []
    for i in range(h):
        row = list(input().strip())
        jail.append(row)
        
        for j in range(w):
            if row[j] == '$':
                prisoner.append((i, j))
    
    # 맵 확장 (상근이를 위해)
    extended_h, extended_w = h + 2, w + 2
    extended_jail = [['.' for _ in range(extended_w)] for _ in range(extended_h)]
    
    # 원래 맵을 확장된 맵 중앙에 복사
    for i in range(h):
        for j in range(w):
            extended_jail[i+1][j+1] = jail[i][j]
    
    # 1. 죄수1에서 BFS (좌표 +1)
    dist1 = bfs_01([(prisoner[0][0]+1, prisoner[0][1]+1)], extended_jail, extended_h, extended_w)
    
    # 2. 죄수2에서 BFS (좌표 +1)
    dist2 = bfs_01([(prisoner[1][0]+1, prisoner[1][1]+1)], extended_jail, extended_h, extended_w)
    
    # 3. 상근이(확장된 맵의 테두리)에서 BFS
    dist_outside = bfs_01([(0,0)], extended_jail, extended_h, extended_w)
    
    # 4. 원래 맵 영역에서만 최솟값 찾기
    min_result = INF
    for i in range(1, extended_h-1):  # 원래 맵 영역만
        for j in range(1, extended_w-1):
            if extended_jail[i][j] != '*':
                total_cost = dist1[i][j] + dist2[i][j] + dist_outside[i][j]
            
                # 문 위치에서 만나는 경우 중복 계산 제거
                if extended_jail[i][j] == '#':
                    total_cost -= 2
                
                min_result = min(min_result, total_cost)
                
    print(min_result)
