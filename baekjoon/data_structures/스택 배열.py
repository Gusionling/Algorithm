import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

array = []
result = []
for _ in range(N):
    array.append(int(input()))

idx = 1
nums = deque()
nums.append(idx)

isPossible = True
for num in array:
    is_exec = False
    
    
    while idx <= N and idx <= num:
        nums.append(idx)
        idx += 1
        result.append('+')
        is_exec = True
        
    if num == nums[-1]:
        nums.pop()
        result.append('-')
        is_exec = True
    
    if not is_exec:
        isPossible = False
        break

if not isPossible:
    print('NO')
else:
    print('\n'.join(result))
