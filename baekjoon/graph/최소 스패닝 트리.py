import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, [cost, a, b])

parent = list(i for i in range(V+1))
rank = [0] * (V+1)  # rank 배열 추가

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a != root_b:
        # rank가 낮은 트리를 rank가 높은 트리 밑에 붙임
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            # 만약 두 트리의 rank가 같다면, 합친 후 rank 증가
            if rank[root_a] == rank[root_b]:
                rank[root_a] += 1

result = 0  # 최소 신장 트리의 가중치 합
edge_num = 0  # 선택된 간선의 개수

while edge_num < V-1:
    if not edges:  # 간선이 부족한 경우 처리
        break
    
    cost, a, b = heapq.heappop(edges)

    # 사이클 확인
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        edge_num += 1

print(result)