import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

# visited[i] = i 위치에 도달하는 최단 시간 (-1이면 미방문)
visited = [-1] * 100001
# count[i] = i 위치에 최단 시간으로 도달하는 경우의 수
count = [0] * 100001

def bfs():
    queue = deque([N])  # deque([N])로 수정!
    visited[N] = 0      # 시작점은 시간 0
    count[N] = 1        # 시작점 경우의 수는 1
    
    while queue:
        current = queue.popleft()
        
        # 목표 지점에 도달한 경우
        if current == K:
            continue
            
        # 세 가지 이동 방법
        next_positions = []
        
        # 1. 걷기: X-1
        if current - 1 >= 0:
            next_positions.append(current - 1)
        
        # 2. 걷기: X+1  
        if current + 1 <= 100000:
            next_positions.append(current + 1)
            
        # 3. 순간이동: 2*X
        if current * 2 <= 100000:
            next_positions.append(current * 2)
        
        # 각 다음 위치에 대해 처리
        for next_pos in next_positions:
            next_time = visited[current] + 1
            
            if visited[next_pos] == -1:  # 처음 방문
                visited[next_pos] = next_time
                count[next_pos] = count[current]
                queue.append(next_pos)
                
            elif visited[next_pos] == next_time:  # 같은 시간에 재방문
                count[next_pos] += count[current]
                # 큐에는 추가하지 않음!

bfs()

print(visited[K])  # 최단 시간
print(count[K])    # 경우의 수