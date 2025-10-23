import sys

input = sys.stdin.readline

N = int(input())

w = []

for _ in range(N):
    w.append(list(map(int, input().split())))

INF = float('inf')
DP = [[INF] * (1<<N) for _ in range(N)]

# 시작점을 0번 도시로 고정
DP[0][1] = 0

for mask in range(1<<N):
    for cur in range(N):
        # 방문한적이 없다면 
        if DP[cur][mask] == INF:
            continue
        # 현재 mask에서 cur이 없을 경우
        if not (mask & (1 << cur)):
            continue
        
        #다음 방문 노드 체크
        for j in range(N):
            # 이미 방문한 도시라면 패스
            if mask & (1 << j):
                continue
            # cur에서 j 까지 경로가 없다면 패스
            if w[cur][j] == 0:
                continue
            
            next_mask = mask | (1<<j)
            DP[j][next_mask] = min(DP[j][next_mask], DP[cur][mask] + w[cur][j])
            
all_visited = (1 <<N) -1
result = INF

for i in range(1, N):
    # 0번 도시에서 출발했는데 0번도시로 돌아갈 길이 없는 경우
    if w[i][0] == 0:
        continue
    result = min(result, DP[i][all_visited] + w[i][0])
    
print(result)
