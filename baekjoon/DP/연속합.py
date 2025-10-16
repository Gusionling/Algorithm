import sys
input = sys.stdin.readline

N = int(input())
# DP의 각 자리는 이어지거나 새로 시작하거나이다. 새로 시작하는 경우는 현재까지의 합이 0이상이기만 하면 오케이이다.
INF = -float('inf')
DP = [INF] * N
nums = list(map(int, input().split()))

DP[0] = nums[0]
# 양수일때만 더해가기 음수가 나오는 순간 바로 

for i in range(1,N):
    # 음수라면 버리는게 나은 선택
    if DP[i-1] < 0:
        DP[i] = nums[i] 
    # 이어가기
    else:
        DP[i] = DP[i-1] + nums[i]

print(max(DP))
