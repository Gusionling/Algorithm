import sys
input = sys.stdin.readline

# 그냥 일단 문제만 보면 그리디이다. 정렬도 여러번 해야한다.
# 파이썬의 팀소트는 빠른 편이기 때문에... 그냥 우선순위 큐를 쓴다면? -> 좋은데...?


T = int(input())

for _ in range(T):
    K = int(input())

    File = [0] + list(map(int, input().split()))
    sum_val = [0] * (K+1)
    
    for f in File:
        sum_val.append(sum_val[-1] + f)

    dp = [[0] * (K+1) for _ in range(K+1)]
    
    for length in range(1,K):
        for start in range(1, K-length+1):
            end = start + length
            
            MIN = sys.maxsize
            for mid in range(start, end):
                MIN = min(MIN, dp[start][mid] + dp[mid+1][end])
                
                dp[start][end] = MIN + sum_val[end] - sum_val[start-1]
                
    print(dp[1][K])