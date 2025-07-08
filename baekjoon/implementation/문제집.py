import heapq
from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

in_degree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
    
pq = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        heapq.heappush(pq, i)
        
result = []

while pq:
    current = heapq.heappop(pq)
    result.append(current)
    
    for next_problem in graph[current]:
        in_degree[next_problem] -= 1
        
        if in_degree[next_problem] == 0:
            heapq.heappush(pq, next_problem)

    
print(" ".join(map(str, result)))
