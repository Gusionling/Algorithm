import sys

input = sys.stdin.readline

# state를 설정 가로 : 0, 세로 : 1, 대각선 : 2

N = int(input())
array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

# DP[i][j][state] - (i,j) 위치에 state 방향으로 파이프가 놓인 경우의 수
DP = [[[0] * 3 for _ in range(N+1)] for _ in range(N+1)]

# 초기 조건: (1,1)과 (1,2)에 가로로 파이프가 놓여있음 (1-indexed)
DP[1][2][0] = 1

# 첫 번째 행 처리 (가로로만 이동 가능)
for j in range(3, N+1):
    if array[1-1][j-1] == 0:  # 벽이 아니면
        DP[1][j][0] = DP[1][j-1][0]

for i in range(2, N+1):
    for j in range(2, N+1):
        
        # 현재 위치가 벽인 경우에는 스킵
        if array[i-1][j-1] == 1:
            continue
        
        # 가로 파이프로 도달하는 경우
        # 이전 위치에서 가로 또는 대각선으로 와서 가로로 놓기
        if j > 1:  # 경계 체크
            DP[i][j][0] = DP[i][j-1][0] + DP[i][j-1][2]
        
        # 세로 파이프로 도달하는 경우
        # 이전 위치에서 세로 또는 대각선으로 와서 세로로 놓기
        if i > 1:  # 경계 체크
            DP[i][j][1] = DP[i-1][j][1] + DP[i-1][j][2]
        
        # 대각선 파이프로 도달하는 경우
        # 대각선으로 이동하려면 (i,j), (i-1,j), (i,j-1) 모두 비어있어야 함
        if i > 1 and j > 1:  # 경계 체크
            if array[i-1][j-2] == 0 and array[i-2][j-1] == 0:  # (i-1,j)와 (i,j-1) 체크
                DP[i][j][2] = DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]

# 결과: (N,N) 위치에 도달하는 모든 경우의 수
result = sum(DP[N][N])
#for i in range(1,N+1):
#    for j in range(1, N+1):
#        print(sum(DP[i][j]), end=" ")
#    print()

print(result)