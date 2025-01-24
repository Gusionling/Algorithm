import sys
input = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int, input().split()))  # 인덱스 1부터 시작
total_max = 0  # 바이토닉 수열의 최대 길이 저장

for i in range(1, N + 1):
    # 증가하는 부분 수열 
    DP = [1] * (N + 1)  # 증가 DP 배열 초기화
    for j in range(1, i + 1):  # 현재 i까지 증가 수열 계산
        for k in range(1, j):
            if nums[k] < nums[j]:
                DP[j] = max(DP[j], DP[k] + 1)

    # 현재까지의 최대값과 해당 인덱스 찾기
    max_length = max(DP[:i + 1])
    idx = DP.index(max_length)

    # 감소하는 부분 수열 
    MIN_DP = [1] * (N + 1)  # 감소 DP 배열 초기화
    for j in range(idx, N + 1):  # idx부터 끝까지 감소 수열 계산
        for k in range(idx, j):
            if nums[k] > nums[j]:
                MIN_DP[j] = max(MIN_DP[j], MIN_DP[k] + 1)
    
    MIN_DP_Length = max(MIN_DP[idx:])

    # 현재 바이토닉 수열 길이 계산 및 최댓값 업데이트 (동일한 곳에서 시작하니까 겹치는거 한번 뺴줌)
    total_max = max(total_max, max_length + MIN_DP_Length - 1)

print(total_max)