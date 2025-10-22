import sys
from collections import deque
input = sys.stdin.readline

dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(start_r, start_c, h, w, room):
    """start 위치에서 모든 칸까지의 최단거리 계산"""
    visited = [[-1] * w for _ in range(h)]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = 0
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < h and 0 <= nc < w and visited[nr][nc] == -1 and room[nr][nc] != 'x':
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    
    return visited

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    room = []
    start = None
    dirties = []
    
    for i in range(h):
        row = list(input().strip())
        room.append(row)
        
        for j in range(w):
            if row[j] == 'o':
                start = (i, j)
            elif row[j] == '*':
                dirties.append((i, j))
    
    dirty_num = len(dirties)
    
    # 1단계: 시작점에서 BFS
    dist_from_start = bfs(start[0], start[1], h, w, room)
    
    # 2단계: 각 더러운 칸에서 BFS하여 거리 행렬 만들기
    dist = [[float('inf')] * dirty_num for _ in range(dirty_num)]
    start_to_dirty = []
    
    possible = True
    
    for i in range(dirty_num):
        d = dist_from_start[dirties[i][0]][dirties[i][1]]
        if d == -1:
            possible = False
            break
        start_to_dirty.append(d)
        
        # i번 더러운 칸에서 다른 더러운 칸들까지의 거리
        temp_dist = bfs(dirties[i][0], dirties[i][1], h, w, room)
        
        for j in range(dirty_num):
            if i != j:
                d = temp_dist[dirties[j][0]][dirties[j][1]]
                if d == -1:
                    possible = False
                    break
                dist[i][j] = d
        
        if not possible:
            break
    
    if not possible:
        print(-1)
        continue
    
    # 3단계: 비트마스킹 DP
    INF = float('inf')
    # dp[현재 더러운 칸 번호][방문한 더러운 칸 집합(비트마스크)]
    dp = [[INF] * (1 << dirty_num) for _ in range(dirty_num)]
    
    # 초기화: 시작점에서 각 더러운 칸으로 직행
    for i in range(dirty_num):
        dp[i][1 << i] = start_to_dirty[i]  # i번만 방문한 상태
    
    # DP 진행
    # 이 부분은 현재 방문 경로로 들어갔을 때 방문하지 않은 모든 더티 노드에 대해서 값을 계산하고 dp만을 업데이트 하는 거다. 
    # 그다음 마스킹에는 영향을 주지는 않는다.
    for mask in range(1 << dirty_num):  # 모든 방문 상태
        for cur in range(dirty_num):  # 현재 위치
            if not (mask & (1 << cur)):  # cur이 방문되지 않았으면 스킵
                continue
            
            if dp[cur][mask] == INF:
                continue
            
            # 다음 방문할 더러운 칸 선택
            for nxt in range(dirty_num):
                if mask & (1 << nxt):  # 이미 방문했으면 스킵
                    continue
                
                new_mask = mask | (1 << nxt)  # nxt 방문 표시
                dp[nxt][new_mask] = min(dp[nxt][new_mask], 
                                        dp[cur][mask] + dist[cur][nxt])
    
    # 4단계: 모든 더러운 칸을 방문한 상태 중 최소값 찾기
    all_visited = (1 << dirty_num) - 1  # 111...1 (모두 방문)
    answer = INF
    
    for i in range(dirty_num):
        answer = min(answer, dp[i][all_visited])
    
    print(answer if answer != INF else -1)