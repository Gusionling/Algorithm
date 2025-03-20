import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

# 상어의 초기 위치 찾기
def find_shark():
    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                sea[i][j] = 0  # 상어 위치를 0으로 초기화
                return i, j
    return -1, -1

# 방향: 위, 왼쪽, 오른쪽, 아래
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def find_nearest_fish(y, x, size):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(y, x, 0)])  # (y, x, 거리)
    visited[y][x] = True
    
    edible_fish = []  # 먹을 수 있는 물고기 목록: (거리, y, x)
    
    while queue:
        cy, cx, dist = queue.popleft()
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            
            # 범위 내에 있고 방문하지 않았는지 확인
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 지나갈 수 있는 칸인지 확인 (크기가 0이거나 상어 크기 이하)
                if sea[ny][nx] <= size:
                    visited[ny][nx] = True
                    queue.append((ny, nx, dist + 1))
                    
                    # 상어보다 작은 물고기가 있는 경우, 먹을 수 있음
                    if 1 <= sea[ny][nx] < size:
                        edible_fish.append((dist + 1, ny, nx))
    
    # 거리, y좌표, x좌표 순으로 정렬
    edible_fish.sort()
    
    return edible_fish[0] if edible_fish else None

def simulate():
    shark_y, shark_x = find_shark()
    shark_size = 2
    fish_eaten = 0
    total_time = 0
    
    while True:
        # 가장 가까운 먹을 수 있는 물고기 찾기
        result = find_nearest_fish(shark_y, shark_x, shark_size)
        
        if not result:
            break  # 더 이상 먹을 수 있는 물고기가 없음
            
        dist, fish_y, fish_x = result
        
        # 상어 위치 업데이트
        shark_y, shark_x = fish_y, fish_x
        
        # 물고기 먹기
        sea[fish_y][fish_x] = 0
        fish_eaten += 1
        
        # 필요한 경우 상어 크기 업데이트
        if fish_eaten == shark_size:
            shark_size += 1
            fish_eaten = 0
            
        # 이동 거리를 총 시간에 추가
        total_time += dist
        
    return total_time

print(simulate())