import sys
input = sys.stdin.readline

N, L = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

result = 0

# 행 검사
for i in range(N):
    row_visited = [False] * N
    possible = True
    
    for j in range(N):
        if j != 0:
            # 높이가 다를 때
            if grid[i][j] != grid[i][j-1]:
                diff = abs(grid[i][j] - grid[i][j-1])
                
                # 높이 차이가 1이 아니면 불가능
                if diff != 1:
                    possible = False
                    break
                
                # 높이가 낮아졌을 때 (앞으로 L개 경사로)
                if grid[i][j] < grid[i][j-1]:
                    for k in range(L):
                        if j+k >= N or row_visited[j+k] or grid[i][j+k] != grid[i][j]:
                            possible = False
                            break
                        row_visited[j+k] = True
                    if not possible:
                        break
                
                # 높이가 높아졌을 때 (뒤로 L개 경사로)
                else:
                    for k in range(L):
                        if j-1-k < 0 or row_visited[j-1-k] or grid[i][j-1-k] != grid[i][j-1]:
                            possible = False
                            break
                        row_visited[j-1-k] = True
                    if not possible:
                        break
    
    if possible:
        result += 1

# 열 검사
for j in range(N):
    col_visited = [False] * N
    possible = True
    
    for i in range(N):
        if i != 0:
            # 높이가 다를 때
            if grid[i][j] != grid[i-1][j]:
                diff = abs(grid[i][j] - grid[i-1][j])
                
                # 높이 차이가 1이 아니면 불가능
                if diff != 1:
                    possible = False
                    break
                
                # 높이가 낮아졌을 때 (아래로 L개 경사로)
                if grid[i][j] < grid[i-1][j]:
                    for k in range(L):
                        if i+k >= N or col_visited[i+k] or grid[i+k][j] != grid[i][j]:
                            possible = False
                            break
                        col_visited[i+k] = True
                    if not possible:
                        break
                
                # 높이가 높아졌을 때 (위로 L개 경사로)
                else:
                    for k in range(L):
                        if i-1-k < 0 or col_visited[i-1-k] or grid[i-1-k][j] != grid[i-1][j]:
                            possible = False
                            break
                        col_visited[i-1-k] = True
                    if not possible:
                        break
    
    if possible:
        result += 1

print(result)