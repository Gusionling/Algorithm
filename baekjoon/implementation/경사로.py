import sys
input = sys.stdin.readline

# 경사로를 고려해야하는 경우 : 높이가 변할 때
# L 의 길이에 따라 구현 조건이 붙게 된다.

N, L = map(int,input().split())

grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))
    

result = 0
for i in range(N):
    # 경사로를 놓은 위치 기억
    row_visited = [False] * N
    for j in range(N):
        # 행
        if j != 0 and row_visited[j] == False:
            # 높이가 달라졌을 때 
            if grid[i][j] != grid[i][j-1]:
                diff = abs(grid[i][j] - grid[i][j-1])
                # 높이차가 1이 아니라면 바로 빠꾸
                if diff != 1:
                    break
                # 높이차이가 1인 경우
                else:
                    # 높이가 낮아졌을때 
                    if diff <0: 
                        for k in range(1,L):
                            if j+k < N and grid[i][j+k] == grid[i][j]:
                                row_visited[j+k] = True
                            else:
                                print(f'{i},{j} 탈출')
                                print(row_visited)
                                break
                        break
                    # 높이가 높아졌을 때 
                    else:
                        for k in range(1,L+1):
                            if j-k > 0 and row_visited[j-k] == False and grid[i][j-k] == grid[i][j-1]:
                                row_visited[j-k] = True
                            else:
                                print(f'{i},{j} 탈출')
                                print(row_visited)
                                break
                        break
        if j == N-1:
            print(f'row : {i} 번째')
            result += 1

#열
for j in range(N):
    # 경사로를 놓은 위치 기억
    col_visited = [False] * N
    for i in range(N):
        # 행
        if i != 0 and  col_visited[i] == False:
            # 높이가 달라졌을 때 
            if grid[i][j] != grid[i-1][j]:
                diff = abs(grid[i][j] - grid[i-1][j])
                # 높이차가 1이 아니라면 바로 빠꾸
                if diff != 1:
                    break
                # 높이차이가 1인 경우
                else:
                    # 높이가 낮아졌을때 
                    if diff <0: 
                        for k in range(1,L):
                            if i+k < N and grid[i+k][j] == grid[i][j]:
                                col_visited[i+k] = True
                            else:
                                print(f'{i},{j} 탈출')
                                print(col_visited)
                                
                                break
                        break
                    # 높이가 높아졌을 때 
                    else:
                        for k in range(1,L+1):
                            if i-k > 0 and col_visited[i-k] == False and grid[i-k][j] == grid[i-1][j]:
                                col_visited[i-k] = True
                            else:
                                print(f'{i},{j} 탈출')
                                print(col_visited)
                                
                                break
                        break
        if i == N-1:
            print(f'col : {j} 번째')
            result += 1

                        
print(result)                       