import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

# union_board는 당일 방문 여부 및 연합 번호를 기록합니다.
union_board = [[0] * N for _ in range(N)]

def BFS(union_board, countries, queue, union_num):
    # 연합에 속한 칸을 저장할 리스트 (내부에서만 업데이트)
    union_cells = []
    
    # 시작 칸 처리
    r, c = queue[-1]
    union_board[r][c] = union_num
    union_cells.append((r, c))
    
    country_sum = countries[r][c]
    country_num = 1

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        row, col = queue.popleft()
        
        for i in range(4):
            nx, ny = row + dx[i], col + dy[i]
            if 0 <= nx < N and 0 <= ny < N and union_board[nx][ny] == 0:
                # 인구 차이가 [L, R] 조건을 만족하면 연합에 포함
                if L <= abs(countries[row][col] - countries[nx][ny]) <= R:
                    union_board[nx][ny] = union_num
                    queue.append((nx, ny))
                    union_cells.append((nx, ny))
                    country_sum += countries[nx][ny]
                    country_num += 1
    
    # 연합이 2개 이상의 칸으로 구성되었을 경우에만 인구 이동
    if country_num > 1:
        avg_sum = country_sum // country_num
        for x, y in union_cells:
            countries[x][y] = avg_sum
        return True  # 연합 형성이 있었음
    return False     # 연합 형성이 없었음 (단일 칸)

days = 0
while True:
    union_formed = False
    union_num = 1
    
    # 하루마다 union_board를 초기화
    union_board = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if union_board[i][j] == 0:
                queue = deque([(i, j)])
                # BFS 실행 후, 연합 형성이 되었으면 union_formed를 True로 변경
                if BFS(union_board, countries, queue, union_num):
                    union_formed = True
                union_num += 1
                
    # 하루 동안 하나의 연합도 형성되지 않았다면 종료
    if not union_formed:
        break
    
    days += 1

print(days)