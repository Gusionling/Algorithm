import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))
m = int(input())

# DP 테이블 초기화
dp = [[False] * n for _ in range(n)]

# 길이 1인 팰린드롬 (모든 단일 문자는 팰린드롬)
for i in range(n):
   dp[i][i] = True

# 길이 2인 팰린드롬
for i in range(n - 1):
   if arr[i] == arr[i + 1]:
       dp[i][i + 1] = True

# 길이 3 이상인 팰린드롬
for length in range(3, n + 1):  # 길이 3부터 n까지
   for i in range(n - length + 1):
       j = i + length - 1
       if arr[i] == arr[j] and dp[i + 1][j - 1]:
           dp[i][j] = True

# 쿼리 처리
for _ in range(m):
   s, e = map(int, input().split())
   print(1 if dp[s - 1][e - 1] else 0)