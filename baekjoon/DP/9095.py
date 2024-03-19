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
        #1이 들어갈 수 있는 자릿수 dp[i-1] 
        #2가 하나 차고 만들어질 수 있는 가짓수 dp[i-2]
        #3이 하나 차고 만들어질 수 있는 가짓수 dp[i-3]
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])



