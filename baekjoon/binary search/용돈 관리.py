import sys

input = sys.stdin.readline

N, M = map(int, input().split())

days = []
for _ in range(N):
    days.append(int(input()))
    
    
right = 10000
left = 0

while left <= right:
    
    mid = (left + right) // 2
    count = 1
    money = mid
    
    for day in days:
        if day > money:
            if day > mid:
                count = M + 1
                break
            money = mid - day
            count += 1
        else:
            money -= day
    
    if count <= M:
        answer = mid
        right = mid - 1
        
    else:
        left = mid + 1

print(answer)
        
        
    