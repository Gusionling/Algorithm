n = int(input())

# 행렬의 차원을 저장 (i번째 행렬은 p[i-1] x p[i]의 크기)
p = [0] * (n+1)
for i in range(n):
    r, c = map(int, input().split())
    if i == 0:
        p[0] = r
    p[i+1] = c

dp = [[0] * n for _ in range(n)]

for length in range(2, n+1):
    for i in range(n - length + 1): # 시작점
        j = i + length -1 # 끝점
        dp[i][j] = float('inf')

        for k in range(i,j):
            cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
            dp[i][j] = min(dp[i][j] , cost)
            
print(dp[0][n-1])
