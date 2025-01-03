from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

N, M = map(int, input().split())

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
count = 0

# 모든 노드를 순회하며 연결 요소 카운트
for node in range(1, N + 1):
    if not visited[node]:
        bfs(node, graph, visited)
        count += 1

print(count)