import sys

input = sys.stdin.readline


N = int(input())
cities = list(map(int, input().split()))
budget = int(input())
cities.sort()

def assingment():
    left = 0
    right = cities[-1]
    
    if sum(cities) <= budget:
        return right
    
    else:
        able = 0
        while left <= right:
            mid = (left + right)//2
            total = 0
            
            
            for city in cities:
                if city >= mid:
                    total += mid
                else:
                    total += city
            
            if total > budget:
                right = mid -1
            else:
                able = mid
                left = mid + 1
                
        return able 

print(assingment())