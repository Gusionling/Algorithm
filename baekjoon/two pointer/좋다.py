import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
result = 0

# 음수일수도 있어서 right를 N-1부터 시작해야한다.
for i in range(N):  # 모든 인덱스 확인
    left, right = 0, N-1
    
    while left < right:
        # 자기 자신은 제외
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
            
        if nums[i] > nums[left] + nums[right]:
            left += 1
        elif nums[i] < nums[left] + nums[right]:
            right -= 1
        else:
            result += 1
            break

print(result)