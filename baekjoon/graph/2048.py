import sys
import copy

input = sys.stdin.readline

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 최대값을 저장할 변수
max_value = 0

def move(dir, current_board):
    # dir : 0 -> 동, 1 -> 서, 2 -> 남, 3 -> 북
    board_copy = copy.deepcopy(current_board)
    
    # 동쪽으로 이동 (오른쪽으로)
    if dir == 0:
        for i in range(N):
            # 먼저 0을 제외한 모든 숫자 추출
            row = [board_copy[i][j] for j in range(N) if board_copy[i][j] != 0]
            # 빈 칸 먼저 채우기
            row = [0] * (N - len(row)) + row
            
            # 오른쪽에서 왼쪽으로 합치기
            for j in range(N-1, 0, -1):
                if row[j] == row[j-1] and row[j] != 0:
                    row[j] *= 2
                    row[j-1] = 0
            
            # 다시 0을 제외한 숫자들 추출
            new_row = [row[j] for j in range(N) if row[j] != 0]
            # 빈 칸 채우기
            new_row = [0] * (N - len(new_row)) + new_row
            
            # 보드에 반영
            board_copy[i] = new_row
    
    # 서쪽으로 이동 (왼쪽으로)
    elif dir == 1:
        for i in range(N):
            # 먼저 0을 제외한 모든 숫자 추출
            row = [board_copy[i][j] for j in range(N) if board_copy[i][j] != 0]
            # 빈 칸 먼저 채우기
            row = row + [0] * (N - len(row))
            
            # 왼쪽에서 오른쪽으로 합치기
            for j in range(N-1):
                if row[j] == row[j+1] and row[j] != 0:
                    row[j] *= 2
                    row[j+1] = 0
            
            # 다시 0을 제외한 숫자들 추출
            new_row = [row[j] for j in range(N) if row[j] != 0]
            # 빈 칸 채우기
            new_row = new_row + [0] * (N - len(new_row))
            
            # 보드에 반영
            board_copy[i] = new_row
    
    # 남쪽으로 이동 (아래로)
    elif dir == 2:
        for j in range(N):
            # 열 추출
            col = [board_copy[i][j] for i in range(N) if board_copy[i][j] != 0]
            # 빈 칸 먼저 채우기
            col = [0] * (N - len(col)) + col
            
            # 아래에서 위로 합치기
            for i in range(N-1, 0, -1):
                if col[i] == col[i-1] and col[i] != 0:
                    col[i] *= 2
                    col[i-1] = 0
            
            # 다시 0을 제외한 숫자들 추출
            new_col = [col[i] for i in range(N) if col[i] != 0]
            # 빈 칸 채우기
            new_col = [0] * (N - len(new_col)) + new_col
            
            # 보드에 반영
            for i in range(N):
                board_copy[i][j] = new_col[i]
    
    # 북쪽으로 이동 (위로)
    else:  # dir == 3
        for j in range(N):
            # 열 추출
            col = [board_copy[i][j] for i in range(N) if board_copy[i][j] != 0]
            # 빈 칸 먼저 채우기
            col = col + [0] * (N - len(col))
            
            # 위에서 아래로 합치기
            for i in range(N-1):
                if col[i] == col[i+1] and col[i] != 0:
                    col[i] *= 2
                    col[i+1] = 0
            
            # 다시 0을 제외한 숫자들 추출
            new_col = [col[i] for i in range(N) if col[i] != 0]
            # 빈 칸 채우기
            new_col = new_col + [0] * (N - len(new_col))
            
            # 보드에 반영
            for i in range(N):
                board_copy[i][j] = new_col[i]
    
    return board_copy

# 모든 경우의 수 탐색 (중첩 반복문을 이용한 완전탐색)
def dfs(depth, current_board):
    global max_value
    
    # 5번 이동한 경우 최대값 갱신
    if depth == 5:
        for i in range(N):
            for j in range(N):
                max_value = max(max_value, current_board[i][j])
        return
    
    # 4방향 이동 시도
    for i in range(4):
        next_board = move(i, current_board)
        dfs(depth + 1, next_board)

# DFS로 완전탐색 시작
dfs(0, board)
print(max_value)