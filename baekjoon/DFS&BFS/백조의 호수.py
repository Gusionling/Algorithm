import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
R, C = map(int, input().split())
lake = []
swan = []
water_queue = deque()  # 물 확산용 큐 (현재 물인 위치들)
swan_queue = deque()   # 백조 이동용 큐 (현재 백조가 도달 가능한 위치들)

# 격자 정보 입력 및 초기 설정
for i in range(R):
    row = list(input().strip())  # list로 변환하여 수정 가능하게
    for j in range(C):
        if row[j] == 'L':
            swan.append((i, j))
        if row[j] != 'X':  # 물이거나 백조인 경우 (이동 가능한 공간)
            water_queue.append((i, j))
    lake.append(row)

# 백조 이동 시작점 설정
swan_queue.append(swan[0])
visited = [[False] * C for _ in range(R)]
visited[swan[0][0]][swan[0][1]] = True

# 방향 벡터 (상, 하, 좌, 우)
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

day = 0
while True:
    # === 1단계: 백조 BFS (현재 이동 가능한 모든 곳 탐색) ===
    next_swan_queue = deque()
    
    while swan_queue:
        r, c = swan_queue.popleft()
        
        # 목적지 도달 확인
        if r == swan[1][0] and c == swan[1][1]:
            print(day)
            sys.exit()
            
        # 4방향 탐색
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            
            # 경계 검사 및 방문 확인
            if 0 <= mr < R and 0 <= mc < C and not visited[mr][mc]:
                visited[mr][mc] = True
                
                if lake[mr][mc] != 'X':  # 물 또는 백조 공간
                    # 즉시 이동 가능 → 현재 큐에 추가
                    swan_queue.append((mr, mc))
                else:  # 얼음 공간
                    # 다음 날 녹을 예정 → 다음 날 큐에 추가
                    next_swan_queue.append((mr, mc))
    
    # === 2단계: 물 확산 BFS (얼음 녹이기) ===
    next_water_queue = deque()
    
    while water_queue:
        r, c = water_queue.popleft()
        
        # 4방향의 얼음 확인
        for i in range(4):
            mr, mc = r + dr[i], c + dc[i]
            
            # 경계 내의 얼음인 경우
            if 0 <= mr < R and 0 <= mc < C and lake[mr][mc] == 'X':
                lake[mr][mc] = '.'  # 얼음을 물로 변경
                next_water_queue.append((mr, mc))  # 다음 날 물 확산 시작점
    
    # === 3단계: 다음 날 준비 ===
    swan_queue = next_swan_queue    # 백조가 다음에 탐색할 위치들
    water_queue = next_water_queue  # 다음에 물 확산을 시작할 위치들
    day += 1
