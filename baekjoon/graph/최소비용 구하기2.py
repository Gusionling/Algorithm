import sys
import heapq

input = sys.stdin.readline

INF = float(1e9)

n = int(input())
m = int(input())

way = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
path = [0] * (n+1)

for _ in range(m):
    start, target, money = map(int, input().split())
    way[start].append((target, money))
    
s, t = map(int, input().split())
    
def dijkstra(start):
    queue = []
    heapq.heappush(queue, start)
    distance[start] = 0
    
    while queue:
        now = heapq.heappop(queue)
        
        for bus in way[now]:
            next, cost = bus
            if distance[next] > distance[now] + cost:
                path[next] = now
                heapq.heappush(queue, next)
        
dijkstra(s)

print(distance[t])
route = []
i = t
while i != s:
    route.append(i)
    i = path[i]
route.append(s)

print(len(route))
print(' '.join(map(str, reversed(route))))  # 역순으로 출력
