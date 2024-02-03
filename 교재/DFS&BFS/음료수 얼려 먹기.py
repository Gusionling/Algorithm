n, m = map(int, input().split())        

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def is_connect(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1:
        return
    graph[x][y] = 1
    is_connect(x+1, y)
    is_connect(x-1, y)
    is_connect(x, y+1)
    is_connect(x, y-1)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            is_connect(i, j)

print(result)
    