import sys
input = sys.stdin.readline

n = int(input())
wine = [0]  # 0번째 인덱스는 사용하지 않음
for _ in range(n):
    wine.append(int(input()))

# dp[i] = i번째 포도주까지 고려했을 때 최대 포도주 양
dp = [0] * (n + 1)

# 초기값 설정
dp[0] = 0
if n >= 1:
    dp[1] = wine[1]
if n >= 2:
    dp[2] = wine[1] + wine[2]

# 점화식: dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])
for i in range(3, n + 1):
    dp[i] = max(
        dp[i-1],  # i번째 포도주를 마시지 않는 경우
        dp[i-2] + wine[i],  # i-1번째를 마시지 않고 i번째를 마시는 경우
        dp[i-3] + wine[i-1] + wine[i]  # i-2번째를 마시지 않고 i-1, i번째를 마시는 경우
    )

print(dp[n])