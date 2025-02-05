import sys
from collections import Counter

input = sys.stdin.readline

# 입력 받기
N = int(input())
nums = [int(input()) for _ in range(N)]

# 1. 산술평균 (소수점 반올림)
avg = round(sum(nums) / N)

# 2. 중앙값 (중간 인덱스의 값)
nums.sort()
middle = nums[N // 2]

# 3. 최빈값 (여러 개일 경우 두 번째로 작은 값)
count = Counter(nums)
freq = max(count.values())
modes = [key for key, value in count.items() if value == freq]

# 최빈값 출력 조건
mode = modes[0] if len(modes) == 1 else sorted(modes)[1]

# 4. 범위 (최댓값 - 최솟값)
rang = nums[-1] - nums[0]

# 결과 출력
print(avg)
print(middle)
print(mode)
print(rang)