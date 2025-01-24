import sys
input = sys.stdin.readline

N = int(input())
cards = [0] + list(map(int, input().split()))  # 1-based index로 사용하기 위해 앞에 0 추가
DP = [0] * (N + 1)

for i in range(1, N + 1):  # i개의 카드를 구매하는 경우
    for j in range(1, i + 1):  # 마지막으로 구매한 카드팩 크기 (1~i)
        DP[i] = max(DP[i], DP[i - j] + cards[j])

print(DP[N])