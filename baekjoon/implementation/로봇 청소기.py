import sys

input = sys.stdin.readline

N, M = map(int, input().split())
row, col, direction = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

# 북: 0, 동: 1, 남: 2, 서: 3
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

cleaned_count = 0

while True:
    # 현재 위치를 청소한다
    if room[row][col] == 0:
        room[row][col] = 2
        cleaned_count += 1

    can_clean = False
    
    # 주변 4칸 중 청소되지 않은 빈칸 찾기
    for _ in range(4):
        # 반시계 방향으로 회전
        direction = (direction - 1 + 4) % 4
        next_row = row + drow[direction]
        next_col = col + dcol[direction]
        
        if room[next_row][next_col] == 0:
            row, col = next_row, next_col
            can_clean = True
            break
    
    # 주변 4칸 중 청소되지 않은 곳이 없다면
    if not can_clean:
        back_dir = (direction + 2) % 4
        back_row = row + drow[back_dir]
        back_col = col + dcol[back_dir]
        
        # 후진 가능하면 후진
        if 0 <= back_row < N and 0 <= back_col < M and room[back_row][back_col] != 1:
            row, col = back_row, back_col
        else:
            # 후진 불가능하면 종료
            print(cleaned_count)
            break