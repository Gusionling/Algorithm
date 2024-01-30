# DFS 알고리즘 구현을 위한 파이썬 코드

#visited=None : 사용자가 이 인자를 제공하지 않았을 때 기본 값으로 None
def dfs(graph, start, visited=None):
    
    # 사용자가 visited집합을 제공하지 않았을 때 집합을 생성하여 방문한 코드들을 추적하는데 사용
    if visited is None:
        visited = set()

        #현재 노드를 방문 처리
        visited.add(start)

        #현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for next_node in graph[start]:
            if next_node not in visited:
                dfs(graph, next_node, visited)
        
        return visited

#간단한 그래프 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#DFS 실행
visited = dfs(graph, 'A')
print("DFS 방문 순서:", visited)

