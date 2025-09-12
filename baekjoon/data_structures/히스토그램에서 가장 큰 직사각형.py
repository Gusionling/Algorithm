import sys
input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    n = line[0]
    if n == 0:
        break
    
    heights = line[1:]
    
    stack = []
    max_area = 0
    
    # 왼쪽부터 순회
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    # 남은 막대들 처리
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    print(max_area)