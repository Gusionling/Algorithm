import bisect

def solve_lis():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # 방법 1: 첫 번째 코드 스타일 (가장 빠름)
    LIS = []  # 이진 탐색용 배열
    dp = []   # (위치, 값) 저장
    
    for i in range(n):
        pos = bisect.bisect_left(LIS, arr[i])
        
        if pos == len(LIS):
            LIS.append(arr[i])
        else:
            LIS[pos] = arr[i]
        
        dp.append((pos, arr[i]))
    
    # LIS 길이 출력
    print(len(LIS))
    
    # 복원
    last_idx = len(LIS) - 1
    result = []
    
    for i in range(len(dp) - 1, -1, -1):
        if dp[i][0] == last_idx:
            result.append(dp[i][1])
            last_idx -= 1
    
    print(*result[::-1])

solve_lis()