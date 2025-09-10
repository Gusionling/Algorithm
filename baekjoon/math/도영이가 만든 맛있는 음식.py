import sys

input = sys.stdin.readline

N = int(input())
taste = []
for _ in range(N):
    sour, bitter = map(int, input().split())
    taste.append([sour, bitter])

result = float('inf')    

for mask in range(1, 1 << N):
    s = 1
    b = 0
    
    for i in range(N):
        if mask & (1 << i):
            s *= taste[i][0]
            b += taste[i][1]
    result = min(result, abs(s - b))

print(result)    
