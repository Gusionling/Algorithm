import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

#다익스트라를 쓸 것이기 때문에 distanceance 배열
distance=[INF]*(n+1)

#모든 버스들의 노선 정보 입력받기
bus = [[] for i in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append((end, cost))

start, end = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue
        for path in bus[now]:
            end = path[0]
            cost = path[1]

            new_cost = distance[now] + cost
            if new_cost < distance[end]:
                distance[end] = new_cost
                heapq.heappush(q, (new_cost, end))

dijkstra(start)
print(distance[end])


        






