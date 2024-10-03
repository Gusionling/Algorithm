import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1, ]

for idx in range(1, N):
    max_value = 0
    for l in range(idx):
        # 비교 가치가 있는 case
        if arr[idx] > arr[l]:
            if max_value < dp[l]:
                max_value = dp[l]

    # 자기까지 count
    dp.append(max_value + 1)

print(max(dp))


                    



