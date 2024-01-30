from collections import deque

n, m = map(int, input().split())

graph = [] 
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x, y))
    
    #큐가 빌 때까지 반복하기 
    while queue:
        #방문을 했으면 그 요소는 빼져야하는 것이고 
        #빠진 요소에 인접한 요소가 추가된다. 
        #queue에는 앞으로 방문할 요소들만 남게 된다. 빠질 떄 처리할 것을 처리해주면 되는 것이다. 
        x, y = queue.popleft()
        # 상하 좌우 표시 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >=n or ny <0 or ny >= m:
                continue
            # 처음 방문하는 경우에만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))


