import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    dp = [[0] * 3 for _ in range(n)]
    
    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue
    
    # 초기값 설정
    dp[0][0] = 0                 # 선택 안함
    dp[0][1] = stickers[0][0]    # 위쪽 선택
    dp[0][2] = stickers[1][0]    # 아래쪽 선택
    
    for i in range(1, n):
        # 현재 열에서 스티커를 선택하지 않는 경우
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        
        # 현재 열에서 위쪽 스티커를 선택하는 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[0][i]
        
        # 현재 열에서 아래쪽 스티커를 선택하는 경우
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + stickers[1][i]
    
    # 마지막 열에서의 최댓값 출력
    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))