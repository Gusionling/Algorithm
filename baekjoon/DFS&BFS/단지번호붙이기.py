import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = []
visited = list([False] * N for _ in range(N))
apt_num = []


for _ in range(N):
    board.append(list(map(int, input().strip())))

dx, dy = [-1,1,0,0],[0,0,-1,1]

def bfs(visited, board, cx,cy):
    # 군집의 개체 개수
    
    queue = deque([(cx,cy)])
    
    nums = 1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0<=nx<N and 0<= ny <N and visited[ny][nx] == False and board[ny][nx] == 1:
                nums += 1
                visited[ny][nx] = True
                queue.append((nx,ny))
    
    apt_num.append(nums)
            
    

for i in range(N):
    for j in range(N):
        # j 가 x , i 가 y
        if board[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            bfs(visited, board, j, i)
            

print(len(apt_num))
apt_num.sort()
for count in apt_num:
    print(count)