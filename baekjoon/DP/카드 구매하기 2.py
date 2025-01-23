import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
DP = [float('inf')] * (N + 1)  # 무한대 값으로 초기화
DP[0] = 0  # 카드 0개를 구매하는 최소 비용은 0

for i in range(1, N + 1):  # i개의 카드를 구매
    for j in range(1, i + 1):  # 마지막으로 구매한 카드 팩 크기 (1~i)
        DP[i] = min(DP[i], DP[i - j] + cards[j - 1])

print(DP[N])