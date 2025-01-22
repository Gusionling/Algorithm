import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
DP = [0] * (n+1)

DP[0] = array[0]

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            DP[i] = max(DP[i], DP[j] + array[i])
        else:
            DP[i] = max(DP[i], array[i])

print(max(DP))