import sys, heapq

input = sys.stdin.readline
INF = 1e9

N , E = map(int, input().split())
cost = list([] for _ in range(N+1))

for _ in range(E):
    a, b, c = map(int, input().split())
    cost[a].append((b,c))
    cost[b].append((a,c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    heap = [(0,start)]

    while heap:
        d, now = heapq.heappop(heap)
        
        if d > dist:
            continue
        
        for next_node, weight in cost[now]:
            next_dist = d + weight
            if next_dist < dist[next_node]:
                dist[next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))
    
    return dist

# 1, v1, v2에서 시작하는 다익스트라 실행
dist_from_1 = dijkstra(1)
dist_from_v1 = dijkstra(v1)
dist_from_v2 = dijkstra(v2)

# 두 가지 경로: 1->v1->v2->N 또는 1->v2->v1->N
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]

result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)
    
