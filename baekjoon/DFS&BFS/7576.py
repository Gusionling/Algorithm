from collections import deque

INF = int(1e9)  # 이 값을 기준으로 최대값 비교를 수행합니다.

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

one_array = []
count = 0
for i in range(n):  # n행 m열로 접근해야 올바름
    for j in range(m):
        if graph[i][j] == 1:
            one_array.append((i, j))
            count += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    queue = deque(one_array)
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return find_max_positive(graph)

def find_max_positive(nested_graph):
    max_val = 0  # 최대값을 저장할 변수 초기화
    for subgraph in nested_graph:
        for item in subgraph:
            #토마토가 모두 익지 않은 경우 
            if item == 0:
                return -1
            elif item > max_val:  # 현재 최대값보다 큰 양수를 찾으면 갱신
                max_val = item
    # 양수가 하나도 없으면 -1을 반환
    if max_val == 0:
        return -1
    return max_val - 1  # 최초에 1부터 시작했으므로, 실제 최대 거리는 최대값 - 1

if count == m*n:
    print(0)
else:
    print(bfs(graph))
