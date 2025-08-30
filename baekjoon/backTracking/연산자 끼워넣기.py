import sys
import heapq

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
min_results = []
max_results = []
oprs = list(map(int, input().split()))

def cal(idx, oprs, result):
    if idx >= N - 1:
        heapq.heappush(min_results, result)
        heapq.heappush(max_results, -result)
        return
    
    for i in range(4):
        if oprs[i] > 0:  # 연산자가 남아있을 때만
            oprs[i] -= 1  # 연산자 사용
            
            if i == 0:  # 덧셈
                cal(idx + 1, oprs, result + nums[idx + 1])
            elif i == 1:  # 뺄셈
                cal(idx + 1, oprs, result - nums[idx + 1])
            elif i == 2:  # 곱셈
                cal(idx + 1, oprs, result * nums[idx + 1])
            else:  # 나눗셈 (C++14 스타일)
                if result == 0:
                    cal(idx + 1, oprs, 0)
                elif result < 0:
                    # C++14 방식: 음수 → 양수 → 나눗셈 → 음수
                    new_result = -((-result) // nums[idx + 1])
                    cal(idx + 1, oprs, new_result)
                else:
                    # 양수는 일반적인 정수 나눗셈
                    cal(idx + 1, oprs, result // nums[idx + 1])
            
            oprs[i] += 1  # 백트래킹: 연산자 복원

cal(0, oprs, nums[0])

print(-heapq.heappop(max_results))  # 최대값
print(heapq.heappop(min_results))   # 최소값