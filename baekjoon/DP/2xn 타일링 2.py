import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [0] * (n + 1)  # DP 테이블 초기화

# 초기값 설정
dp[1] = 1
if n > 1:
    dp[2] = 3

# 점화식 적용
for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

# 결과 출력
print(dp[n])