import sys

input = sys.stdin.readline
n = int(input())

array = [int(input()) for _ in range(n)]
dp = [1] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4
for num in array:
    for i in range(4, num+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])



