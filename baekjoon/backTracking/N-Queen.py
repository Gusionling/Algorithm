import sys
input = sys.stdin.readline

N = int(input())
board = [False] * N 
cnt = 0


def back(row):

    global cnt

    if row == N:
        cnt += 1
        return
    
    for col in range(N):
        if not visited_cols[col] and not diag1[col - row + N-1] and not diag2[row+col]:
            # 퀸 배치
            visited_cols[col] = diag1[col - row + N-1] =  diag2[row+col] = True

            back(row + 1) # 다음 행으로 진행

            # 백트레킹 (퀸 제거)
            visited_cols[col] = diag1[col - row + N-1] =  diag2[row+col] = False


# 충돌 체크용 배열
visited_cols = [False] * N              # 열 체크
diag1 = [False] * (2 * N - 1)           # / 대각선 (col - row + N - 1)
diag2 = [False] * (2 * N - 1)           # \ 대각선 (row + col)

back(0)
print(cnt)