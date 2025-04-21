import sys

input = sys.stdin.readline

size = int(input())
array = list(map(int, input().split()))


        
def longest_increasing_subsequence(arr):
    if not arr:
        return 0
        
    # L 배열 초기화
    L = [arr[0]]
    
    for num in arr[1:]:
        # 현재 숫자가 L 배열의 마지막 값보다 크면 추가
        if num > L[-1]:
            L.append(num)
        else:
            # 이진 탐색으로 대체할 위치 찾기
            left, right = 0, len(L) - 1
            pos = 0
            
            while left <= right:
                mid = (left + right) // 2
                
                if L[mid] >= num:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 해당 위치의 값을 num으로 대체
            L[pos] = num
    
    # L 배열의 길이가 LIS의 길이
    return len(L)
        
print(array)