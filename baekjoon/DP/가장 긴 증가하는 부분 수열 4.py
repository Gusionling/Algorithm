import sys
import copy

input = sys.stdin.readline

# 입력
N = int(input())
array = list(map(int, input().split()))

# DP 배열과 각 인덱스에서의 수열을 저장할 컨테이너 초기화
DP = [1] * N
Container = [[x] for x in array]  # 각 요소별로 초기화 (자기 자신 포함)

# DP와 Container 계산
for i in range(N):
    for j in range(i):
        if array[i] > array[j] and DP[i] < DP[j] + 1:
            DP[i] = DP[j] + 1
            Container[i] = copy.deepcopy(Container[j])  # j의 수열 복사
            Container[i].append(array[i])  # 현재 요소 추가

# DP 배열에서 최댓값과 해당 인덱스 찾기
max_length = max(DP)
idx = DP.index(max_length)

print(max_length)
print(*Container[idx])