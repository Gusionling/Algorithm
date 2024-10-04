import sys
input = sys.stdin.readline

N = int(input())
# DP 배열 초기화
DP = [[0, float('inf')] for _ in range(3)]

# 첫 번째 행 초기화
first_row = list(map(int, input().split()))
for j in range(3):
    DP[j][0] = first_row[j]  # 최대값
    DP[j][1] = first_row[j]  # 최소값

# DP 계산
for i in range(1, N):
    # 현재 행의 DP 상태를 저장할 리스트
    current = [[0, float('inf')] for _ in range(3)]

    # 입력 받으며 DP 업데이트
    row = list(map(int, input().split()))
    
    for j in range(3):
        # 최대값 계산
        if j == 0:
            current[j][0] = row[j] + max(DP[j][0], DP[j+1][0])
        elif j == 1:
            current[j][0] = row[j] + max(DP[j-1][0], DP[j][0], DP[j+1][0])
        else:  # j == 2
            current[j][0] = row[j] + max(DP[j-1][0], DP[j][0])
        
        # 최소값 계산
        if j == 0:
            current[j][1] = row[j] + min(DP[j][1], DP[j+1][1])
        elif j == 1:
            current[j][1] = row[j] + min(DP[j-1][1], DP[j][1], DP[j+1][1])
        else:  # j == 2
            current[j][1] = row[j] + min(DP[j-1][1], DP[j][1])
    
    # DP 배열 업데이트
    DP = current

# 결과 계산
max_result = max(DP[j][0] for j in range(3))
min_result = min(DP[j][1] for j in range(3))

print(max_result, min_result)
