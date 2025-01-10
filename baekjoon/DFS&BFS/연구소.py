from collections import deque
import copy

n, m = map(int, input().split())
graph = [] 
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 바이러스 퍼지기
def bfs():
    
    tmp_graph = copy.deepcopy(graph)
    queue = deque([(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2])
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))

    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    
    global answer
    answer = max(cnt, answer)

# 백트레킹으로 벽을 놓을 수 있는 위치 조정
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt + 1)
                graph[i][j] = 0 # 다시 벽을 허무는 과정이다.

answer = 0
makeWall(0)
print(answer)



