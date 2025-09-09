import sys
from collections import deque

input = sys.stdin.readline
INF = float('inf')

T = int(input())
dr, dc = (-1,1,0,0) , (0,0,-1,1)


# person 은 두 사람이기에 구별하기 위해 있는 것이고 두번째 사람이라면 구현이 조금더 추가된다.
def bfs(visited, jail, person, prisoner, h, w):
    # 밖으로 나간 case 저장
    result = []
    
    if person == 0:
        queue = deque([prisoner[0]])
    else:
        queue = deque([prisoner[1]])
    
    visited[prisoner[person][0]][prisoner[person][1]][person] = 0
    
    while queue:
        r, c = queue.popleft()
        
        for i in range(4):
            nr , nc = r + dr[i], c + dc[i]
            
            if 0<= nr < h and 0<= nc < w: 
                if jail[nr][nc] != '*' and visited[nr][nc][person] == INF:
                    # 죄수 1호
                    if person == 0:
                        # 벽인경우
                        if jail[nr][nc] == '#':
                            visited[nr][nc][person] = visited[r][c][person] + 1
                        else:
                            visited[nr][nc][person] = visited[r][c][person]
                        
                        queue.append((nr,nc))
                    
                    
                    # 죄수 2호
                    else:
                        # 죄수 1호가 거쳐간 곳이라면 그냥 얹기
                        if visited[nr][nc][0] != INF:
                            visited[nr][nc][1] = visited[r][c][1]
                            
                        else:
                            if jail[nr][nc] == '#':
                                visited[nr][nc][person] = visited[r][c][person] + 1
                            else:
                                visited[nr][nc][person] = visited[r][c][person]
                        
                        queue.append((nr,nc))

            # 밖으로 나간 경우
            else:
                result.append((r, c))
            
                    
    return jail, result, visited                          


for _ in range(T):
    h, w = map(int, input().split())
    prisoner = []
    # visited 는 INF로 초기화 하자
    visited = [[[INF] * 2 for _ in range(w)] for _ in range(h)]
    
    
    # 보드 입력 받기    
    jail = []
    for i in range(h):
        row = list(input().strip())
        jail.append(row)

        for j in range(w):
            if row[j] == '$':
                prisoner.append((i,j))
                
    # BFS 시작
    jail1, result0, visited0 = bfs(visited, jail, 0, prisoner, h, w)
    jail2, result1, visited1 = bfs(visited0, jail1, 1, prisoner, h, w)
    
    print(visited1)
    result = set(result0 + result1)
    
    min_result = INF
    for r,c in result:
        if 0 <= r < h and 0 <= c < w:  # 안전 체크 추가
            sum_val = visited1[r][c][0] + visited1[r][c][1]
            #print(visited1[r][c][0] , visited1[r][c][1])
            min_result = min(sum_val, min_result)
    
    print(min_result)