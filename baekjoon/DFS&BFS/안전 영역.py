import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# 입력된 높이들을 set으로 저장한 후 0(비가 오지 않는 경우)도 추가
heights = set()
for row in area:
    heights.update(row)
heights.add(0)

result = 0

# 각 강수량(비의 높이)에 대해 안전 영역의 개수를 구함
for rain in heights:
    # 현재 강수량으로 침수된 영역은 1, 안전한 영역은 0
    ground = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] <= rain:
                ground[i][j] = 1

    safe_count = 0  # 안전 영역(연결된 0의 영역)의 개수

    for i in range(N):
        for j in range(N):
            # 아직 방문하지 않은 안전한 영역 발견
            if ground[i][j] == 0:
                dq = deque()
                dq.append((i, j))
                ground[i][j] = 1  # 방문 처리

                # BFS를 통해 인접한 안전 영역 모두 방문 처리
                while dq:
                    x, y = dq.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and ground[nx][ny] == 0:
                            ground[nx][ny] = 1
                            dq.append((nx, ny))
                safe_count += 1

    result = max(result, safe_count)

print(result)