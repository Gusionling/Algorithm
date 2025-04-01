import sys

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V+1)]

for i in range(V):
    data = list(map(int, input().split()))
    node = data[0]  # 노드 번호 읽기
    j = 1
    while j < len(data) - 1:  # 마지막 -1 전까지 반복
        dest, cost = data[j], data[j+1]  # 올바른 언패킹 문법
        tree[node].append([cost, dest])
        j += 2

# 트리의 지름을 찾는 함수
def dfs(start):
    # 거리 초기화
    distances = [-1] * (V+1)
    distances[start] = 0
    
    stack = [start]
    while stack:
        current = stack.pop()
        
        for cost, dest in tree[current]:
            # 이미 방문했으면 건너뛰기
            if distances[dest] != -1:
                continue
            
            distances[dest] = distances[current] + cost
            stack.append(dest)
    
    # 가장 먼 노드와 그 거리 찾기
    max_dist = 0
    farthest_node = start
    for i in range(1, V+1):
        if distances[i] > max_dist:
            max_dist = distances[i]
            farthest_node = i
    
    return farthest_node, max_dist

# 첫 번째 DFS: 지름의 한쪽 끝 노드 찾기
any_node = 1
farthest, _ = dfs(any_node)

# 두 번째 DFS: 다른 쪽 끝과 지름의 길이 찾기
_, diameter = dfs(farthest)

print(diameter)