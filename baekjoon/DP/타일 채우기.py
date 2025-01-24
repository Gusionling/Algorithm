import sys

input = sys.stdin.readline

# 입력값
N = int(input())

# 홀수일 경우 답은 0
if N % 2 != 0:
    print(0)
    exit()

# DP 배열 초기화
DP = [0] * (N + 1)
DP[0] = 1
DP[2] = 3 

for i in range(4, N + 1, 2):
    DP[i] = 3 * DP[i - 2]
    for j in range(i - 4, -1, -2):
        DP[i] += 2 * DP[j]


print(DP[N])