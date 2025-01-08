import sys
import heapq

def main():
    V,E = map(int,sys.stdin.readline().strip().split()) # 정점, 간선
    K = int(sys.stdin.readline().strip()) # 시작점

    INF = int(1e9) # 초기값
    graph = [[] for _ in range(V+1)]
    # distance는 정답이 될 리스트 그 자체 계속 look up 을 하면서 비교해봐야할 변수
    distance = [INF] * (V+1)

    for _ in range(E):
        u,v,w = map(int,sys.stdin.readline().strip().split())
        graph[u].append((v,w)) # (정점, 가중치)

    def dijkstra(start): # 최단경로 탐색
        queue = []
        heapq.heappush(queue,(0,start)) # (가중치, 정점)
        distance[start] = 0

        while queue:
            # dist는 queue에 들어가 있는 now라는 정점에 대해 출발점에서 시작한 최단 거리이다. 
            dist,now = heapq.heappop(queue)
            # distance는 아래 fot문 안에서 처리된는 것 처럼 항상 최소값을 유지하고 있다 왜냐하면 고려한 것 모든 것 중에 최소일 때 update하니까
            # 근데 queue에는 그렇지 않다 같은 정점이라 하더라도 나중에 고려하면서 새롭게 최단 거리가 추가 되어 과거에 들어간게 최소들이 아닐 수 있다. 
            # 당연히 새로운 최소거리의 가중치도 그 위치의 정점과 queue에 들어간다. 
            # 그렇기 때문에 아래 코드의 의미는 dist (그냥 과거에서 그당시 최소라고 판단된 거리)가 queue에서 뽑혔을 당시도 최소인지 검증하는 것이다. 
            # 그럼 새 의문이 들 수도 있다 그러면 그 정점에 대해서는 경로를 살펴보지 못하는가? 
            # -> 아니다. 그 정점에 대해서는 distance[now] 가 최소값을 가지게한 case에서 그에 해당하는 가중치와 그 정점이 들어가 있어 처리가 될 것이다. 
            # 그렇기 때문에 아래 코드는 굳이 큐 안에 들어간 요소들 중 불 필요한 것을 거르기 위해 들어간 것이라고 보면 된다. 
            if distance[now] < dist: # 최단 경로가 아니라면
                continue

            for v,w in graph[now]:
                cost = dist + w # 현재 정점까지의 가중치 + 다음 정점까지의 가중치
                if cost < distance[v]: # 현재 정점까지의 가중치가 더 작다면

                    distance[v] = cost
                    heapq.heappush(queue,(cost,v))

    dijkstra(K)

    for num in range(1,V+1):
        if distance[num] == INF:
            print("INF")
        else:
            print(distance[num])


if __name__ == '__main__':
    main()