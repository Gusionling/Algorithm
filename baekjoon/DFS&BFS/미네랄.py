import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

mineral = []
cave = []
for r in range(R):
    row = list(input().strip())
    cave.append(row)
    
    # 미네랄 위치 삽입
    for c in range(C):
        if row[c] == 'x':
            mineral.append((r,c))
            

dr, dc = [-1,1,0,0] , [0,0,-1,1]

N = int(input())

def bfs(start_r, start_c, visited):
    
    queue = deque([(start_r, start_c)])
    mineral_in_cluster = [(start_r, start_c)]
    visited[start_r][start_c] = True
    
    while queue:
        r,c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i] , c + dc[i]
            
            if 0<=nr<R and 0<=nc<C and visited[nr][nc] == False:
                if cave[nr][nc] == 'x':
                    queue.append((nr,nc))
                    mineral_in_cluster.append((nr,nc))
                    visited[nr][nc] = True
                
    return mineral_in_cluster

ways = list(map(int, input().split()))
for turn in range(N):
    height = ways[turn]
    h = R - height
    
    # 짝수인 경우에는 왼쪽에서 던진다.
    if turn % 2 == 0:
        for i in range(C):
            if cave[h][i] == 'x':
                cave[h][i] = '.'
                break
    # 홀수인 경우에는 오른쪽에서 던진다.
    else:
        for i in range(C-1, -1, -1):
            if cave[h][i] == 'x':
                cave[h][i] = '.'
                break
    
    # 바닥부터 연결된 미네랄 찾기
    visited = [[False] * C for _ in range(R)]
    ground_connected = []
    
    for j in range(C):
        if cave[R-1][j] == 'x' and not visited[R-1][j]:
            cluster = bfs(R-1, j, visited)
            ground_connected.extend(cluster)
    
    # 전체 미네랄에서 바닥 연결된 것 빼기 = 떨어질 것들
    all_minerals = []
    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x':
                all_minerals.append((r,c))
    
    falling = list(set(all_minerals) - set(ground_connected))
    
    if falling:
        # 떨어질 미네랄들 지우기
        for r, c in falling:
            cave[r][c] = '.'
        
        # 클러스터가 떨어질 수 있는 최대 거리 계산
        min_drop = float('inf')
        for r, c in falling:
            drop_distance = 0
            new_r = r
            while new_r + 1 < R and cave[new_r + 1][c] == '.':
                new_r += 1
                drop_distance += 1
            min_drop = min(min_drop, drop_distance)
        
        # 클러스터 전체를 min_drop만큼 떨어뜨리기
        for r, c in falling:
            cave[r + min_drop][c] = 'x'

# 출력
for row in cave:
    print(''.join(row))