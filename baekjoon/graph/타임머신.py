import sys

input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
ways = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    ways[start].append((cost, end))

costs = [INF] * (N+1)
costs[1] = 0

# (N-1)번 반복: 최단 거리 갱신
for order in range(N):
    for start in range(1, N+1):
        if costs[start] != INF:  # 도달 가능한 정점만
            for cost, end in ways[start]:
                if costs[end] > costs[start] + cost:  # 조건 수정!
                    if order == N-1:
                        print(-1)
                        exit()
                    costs[end] = costs[start] + cost

for i in range(2, N+1):
    if costs[i] == INF:
        print(-1)
    else:
        print(costs[i])