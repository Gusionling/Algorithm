import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

move = [-1] * (101)
visited = [False] * (101)

for _ in range(N+M):
    x, y = map(int, input().split())
    move[x] = y

queue = deque([(1, 0)])
visited[1] = True

while queue:
    loc, time = queue.popleft()
    
    for i in range(1, 7):
        dx = loc + i
        
        # Check bounds
        if dx > 100:
            continue
            
        # Check if we reached the goal
        if dx == 100:
            print(time + 1)
            exit()  # Exit the entire program
        
        # Skip if already visited
        if visited[dx]:
            continue
            
        # Mark as visited
        visited[dx] = True
        
        # Check if there's a snake or ladder
        if move[dx] != -1:
            next_pos = move[dx]
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
        else:
            queue.append((dx, time + 1))