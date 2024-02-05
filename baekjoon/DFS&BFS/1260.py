from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N+1) for _ in range(N+1)]

#연결된 정점을 입력
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

#방문 리스트 행렬
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

#DFS 
def dfs(V):
    visited1[V] = True
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i] == True and visited1[i] == False:
            dfs(i)

#BFS
def bfs(V):
    queue = [V]
    visited2[V] = True
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visited2[i] == False and graph[V][i] == True):
                queue.append(i)
                visited2[i] = True

dfs(V)
print()
bfs(V)





    

