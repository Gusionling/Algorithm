import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*n
#집들의 정보 받기
dp = [list(map(int, input().split())) for _ in range(n)]

#점화식 아이디어 
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + dp[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

#그간 dp는 한갈래였다. 3갈래의 경우를 따져서 오다니...
#이전 것이 어떤 것인지에 따라 달려있기 때문에 하나씩 다 따져봐야 한다. 
#2번 건널 필요가 없는 것이 위에 처럼 다 처리를 해버리면 쌓아온 것들도 조건을 만족한다. 