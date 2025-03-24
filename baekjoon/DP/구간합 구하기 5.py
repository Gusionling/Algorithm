import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int,input().split()))for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = board[0][0]

# 초기화 
for i in range(1,N):
    DP[0][i] = DP[0][i-1] + board[0][i]
    DP[i][0] = DP[i-1][0] + board[i][0]

# DP update
for i in range(1, N):
    for j in range(1, N):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + board[i][j]

# 계산 결과 구하기
for _ in range(M):
    r1, c1, r2, c2, = map(int,input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

    m1 = DP[r1-1][c2] if r1>0 else 0
    m2 = DP[r2][c1-1] if c1>0 else 0
    plus = DP[r1-1][c1-1] if r1>0 and c1>0 else 0

    result = DP[r2][c2] - m1 - m2 + plus

    print(result)
