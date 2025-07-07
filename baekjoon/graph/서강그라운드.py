import heapq

def solve_dijkstra():
    n, m, r = map(int, input().split())
    items = [0] + list(map(int, input().split()))
    
    # 인접 리스트 구성
    graph = [[] for _ in range(n+1)]
    for _ in range(r):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    
    def dijkstra(start):
        dist = [float('inf')] * (n+1)
        dist[start] = 0
        pq = [(0, start)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        return dist
    
    max_items = 0
    # 각 지역에서 Dijkstra 실행
    for start in range(1, n+1):
        dist = dijkstra(start)
        current_items = 0
        for target in range(1, n+1):
            if dist[target] <= m:
                current_items += items[target]
        max_items = max(max_items, current_items)
    
    print(max_items)

solve_dijkstra()