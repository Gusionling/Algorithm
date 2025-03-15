import sys
import copy
input = sys.stdin.readline

N,M,X,Y,K = map(int, input().split())
# 초기 주사위는 0으로 초기화
dice = [0] * 6

#board 초기화
board = [list(map(int,input().split())) for _ in range(N)]

# 명령 개수
orders = map(int,input().split())

# 동, 서 , 북, 남
dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

dir = [[0]*6 for _ in range(5)]

# 동서북남
dir[1] = [2,0,5,3,4,1]
dir[2] = [1,5,0,3,4,2]
dir[3] = [4,1,2,0,5,3]
dir[4] = [3,1,2,5,0,4]

# 초기 위치 
x, y = Y, X 

for order in orders:
    # 영역 밖으로 나가는지 부터 검즘
    nx, ny = x + dx[order], y + dy[order]
    if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
    # 영역 밖으로 나가지 않은 경우
    # 위치 업데이트
    x, y = nx, ny
    # 주사위의 이동
    i = 0
    new_list = [0] * 6
    for idx in dir[order]:
        new_list[i] = dice[idx] 
        i += 1
    dice = copy.deepcopy(new_list)
    
    # 지도가 0인 경우 
    if board[ny][nx] == 0:    
        # 주사위에 있는게 복사
        board[ny][nx] = dice[0]
    # 지도가 0이 아닌 경우 
    else:
        dice[0] = board[ny][nx]
        board[ny][nx] = 0
    
    print(dice[5])

