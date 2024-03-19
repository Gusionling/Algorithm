from collections import deque

def bfs():
    q = deque()
    # 방문한 노드를 queue에 넣느다. 
    q.append(n)
    while q:
        x = q.popleft()
        if x == k: 
            print(dist[x])
            break
        for nx in (x - 1 ,x + 1, x * 2):
            #처음 방문하는 경우만 Queue에 삽입
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

MAX = 10**5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()

