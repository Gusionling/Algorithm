import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [[0] * N for _ in range(N)]

# 사과 위치 입력
Apples = int(input())
for _ in range(Apples):
    col, row = map(int, input().split())
    board[col-1][row-1] = 1

Turn_Nums = int(input())
turns = deque()
for _ in range(Turn_Nums):
    time, dir = input().split()
    time = int(time)

    turns.append((time,dir))


# 1 로 초기화 하는 이유는 벽에 부딪히는 것도 초로 계산 하기 때문에 
time = 1
# 초기 시작은 (0,0)
snake = deque([(0,0)])
# 북동남서 방향
directions = [(-1,0), (0,1) , (1,0), (0,-1)]
# 초기 방향은 동쪽
d_idx = 1
y, x = snake[-1]

while True:
    ny, nx = y + directions[d_idx][0], x + directions[d_idx][1]

    if 0<=nx<N and 0<=ny<N and (ny,nx) not in snake:
        snake.append((ny,nx)) 
        # 사과가 아닐 때
        if board[ny][nx] == 0:
            snake.popleft()
        # 사과일 때는 꼬리를 빼지 않는다.
        else:
            board[ny][nx] = 0

        # 이동을 완료하고 후처리
        if turns and time == turns[0][0]:
            # 돌아야 될 시간이 된다면 
            _, turn_dir = turns.popleft()
            if turn_dir == 'D':
                d_idx = (d_idx + 1) % 4
            else:
                d_idx = (d_idx - 1) % 4
    else:
        break


    time += 1
    y, x = snake[-1]
    


print(time)
