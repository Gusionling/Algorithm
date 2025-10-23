import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 비용의 총합은 최대 100 * 100 = 10000
max_cost = sum(cost)
DP = [0] * (max_cost + 1)

# 각 앱에 대해
for i in range(N):
    # 뒤에서부터 업데이트 (중복 선택 방지)
    for c in range(max_cost, cost[i] - 1, -1):
        DP[c] = max(DP[c], DP[c - cost[i]] + memory[i])

# M 이상의 메모리를 확보하는 최소 비용 찾기
ans = 0
for c in range(max_cost + 1):
    if DP[c] >= M:
        ans = c
        break

print(ans)