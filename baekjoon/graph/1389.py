import sys
INF = int(1e9)
N, M = map(int,input().split())
graph =[[INF] * (N + 1)  for _ in range(N + 1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1 , N + 1):
            graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])

bacon = INF
answer = 0
# bacom이 동일할 경우 작은 수를 출력하기 위해 역순으로 
for i in range(N, 0, -1):
    #sum은 iterable객체의 합을 나타내준다. 
    s = sum(graph[i][1:])
    if bacon >= s:
        bacon = s
        answer = i
print(answer)