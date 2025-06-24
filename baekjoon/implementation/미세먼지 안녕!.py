import sys, copy
input = sys.stdin.readline

dr, dc = [-1,1,0,0] , [0,0,-1,1]

R, C, T = map(int, input().split())
array = []
for _ in range(R):
    array.append(list(map(int, input().split())))

for i in range(R):
    if array[i][0] == -1:
        up = i
        break

down = up + 1

def spread():
    temp_array = copy.deepcopy(array)
    
    for i in range(R):
        for j in range(C):
            # 4 이하일 경우에는 확산하지 않는다.
            if temp_array[i][j] > 4:
                
                side = temp_array[i][j] // 5
                count = 0
                
                for k in range(4):
                    r,c = i + dr[k], j + dc[k]
                    if 0<= r < R and 0<= c < C and array[r][c] != -1:
                        array[r][c] += side
                        count += 1
                array[i][j] -= side * count

def left(start):
    # 위쪽 공기청정기 - 반시계방향
    # 아래로
    for i in range(start-1, 0, -1):
        array[i][0] = array[i-1][0]
    
    # 오른쪽으로
    for j in range(C-1):
        array[0][j] = array[0][j+1]
    
    # 위로
    for i in range(start):
        array[i][C-1] = array[i+1][C-1]
    
    # 왼쪽으로
    for j in range(C-1, 1, -1):
        array[start][j] = array[start][j-1]
    
    # 공기청정기에서 나오는 바람은 미세먼지 0
    array[start][1] = 0

def right(start):
    # 아래쪽 공기청정기 - 시계방향
    # 위로
    for i in range(start+1, R-1):
        array[i][0] = array[i+1][0]
    
    # 오른쪽으로
    for j in range(C-1):
        array[R-1][j] = array[R-1][j+1]
    
    # 아래로
    for i in range(R-1, start, -1):
        array[i][C-1] = array[i-1][C-1]
    
    # 왼쪽으로
    for j in range(C-1, 1, -1):
        array[start][j] = array[start][j-1]
    
    # 공기청정기에서 나오는 바람은 미세먼지 0
    array[start][1] = 0
        
for _ in range(T):
    spread()
    left(up)
    right(down)

# 결과 계산 (공기청정기 위치 -1은 제외)
result = 0
for i in range(R):
    for j in range(C):
        if array[i][j] > 0:
            result += array[i][j]

print(result)