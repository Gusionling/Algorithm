import sys

input = sys.stdin.readline

N = int(input().split())

w = []

for _ in range(N):
    w.append(list(map(int, input().split())))

INF = float('inf')
DP = list([INF] * N for _ in range(1 << N))

# 시작점을 0번 도시로 고정
DP[1][0] = 0

for mask in range(1<<N):
    for i in range(N):
        if DP[mask][i] == INF:
            continue
        if not (mask & (1 << i)):
            continue
        
        for j in range(N):
            if mask & (1 << j):
                continue
            if w[i][j] == 0:
                continue
            
            next_mask = mask | (1<<j)
            DP[next_mask][j] = min(DP[next_mask][j], DP[mask][i] + w[i][j])
            
all_visited = (1 <<N) -1
result = INF

for i in range(1, N):
    if w[i][0] == 0:
        continue
    result = min(result, DP[all_visited][i] + w[i][0])
    

print(result)




