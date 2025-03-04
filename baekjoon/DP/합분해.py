import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# DP[K][N] = DP[K][N-1] + DP[K-1][N]
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n + 1):
    for j in range(1, k + 1):
        if i == 0:
            dp[i][j] = 1  # k개의 수를 합해서 0을 만드는 경우는 항상 1가지 (모두 0인 경우)
        else:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000
print(dp[n][k] % 1000000000)