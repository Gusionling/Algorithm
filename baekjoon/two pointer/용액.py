import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N - 1
min_sum = sys.maxsize  # 가장 큰 값으로 초기화
min_set = []

while left < right:
    sum_pair = arr[left] + arr[right]

    # 현재 조합이 최소값이면 업데이트
    if abs(sum_pair) < min_sum:
        min_sum = abs(sum_pair)
        min_set = [arr[left], arr[right]]

    # 투 포인터 이동 조건
    if sum_pair < 0:
        left += 1  # 더 큰 값을 찾아야 함
    elif sum_pair > 0:
        right -= 1  # 더 작은 값을 찾아야 함
    else:
        break  # 정확히 0이면 최적해이므로 종료

print(*min_set)