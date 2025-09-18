import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 스택에는 하향 상태를 가지고 값들이 들어간다.
stack = deque()

water = 0

for i in range(len(heights)):
    
    # 하향 상태를 가지고 있는 스택이 갑자기 큰 높이를 만나게 된다면 그곳이 특이점이자 변곡점
    while stack and heights[i] > heights[stack[-1]]:
        
        top = stack.pop()
        
        if not stack:
            break
    
        h = min(heights[i], heights[stack[-1]]) - heights[top]
        w = i - stack[-1] - 1
        water += h * w
        
    
    stack.append(i)

print(water)
            
