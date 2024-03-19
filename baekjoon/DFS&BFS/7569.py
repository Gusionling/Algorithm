from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 첫 줄에 M, N, H를 입력받습니다. split()으로 나누고, 각각 정수형으로 변환합니다.
M, N, H = map(int, input().split())

# 3차원 리스트를 초기화합니다.
tomatoes = []

count = 0

# H개의 높이에 대하여
for _ in range(H):
    # 각 높이마다의 2차원 리스트(박스)를 생성합니다.
    box = []
    for _ in range(N):
        # 각 줄(세로 줄)을 입력받아 정수형 리스트로 변환하여 box에 추가합니다.
        row = list(map(int, input().split()))
        box.append(row)
    # 완성된 2차원 리스트(박스)를 3차원 리스트에 추가합니다.
    tomatoes.append(box)

one_array = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                one_array.append((i,j,k))

def bfs(tomatoes):
    q = deque(one_array)

    while q:
        z,y,x = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= M or ny <0 or ny >=N or nz < 0 or nz>=H:
                continue
            elif tomatoes[nz][ny][nx] == 0:
                tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
                q.append((nz, ny, nx))
    return find_max_positive(tomatoes)

def find_max_positive(nested_graph):
    max_val = 0  # 최대값을 저장할 변수 초기화
    for subgraph in nested_graph:
        for items in subgraph:
            for item in items:
                #토마토가 모두 익지 않은 경우 
                if item == 0:
                    return -1
                elif item > max_val:  # 현재 최대값보다 큰 양수를 찾으면 갱신
                    max_val = item
    # 양수가 하나도 없으면 -1을 반환
    if max_val == 0:
        return -1
    return max_val - 1  # 최초에 1부터 시작했으므로, 실제 최대 거리는 최대값 - 1

if count == M*N*H:
    print(0)
else:
    print(bfs(tomatoes))
