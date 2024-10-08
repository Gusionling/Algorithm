import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
connect = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

visited = [False] * (N+1)
parent = [0] * (N+1)

#BFS
dq = deque([1])
visited

while dq:
    p = dq.popleft()
    visited[p] = True
    for child in connect[p]:
        if visited[child]:
            continue
        parent[child] = p
        dq.append(child)

print("\n".join(map(str, parent[2:])))

