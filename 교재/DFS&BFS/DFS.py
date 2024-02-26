# DFS 알고리즘 구현을 위한 파이썬 코드

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print( v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


#각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [], # 노드의 번호가 1번부터 주어지는 경우가 많이 때문에 인덱스 0번을 비워둔다. 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)