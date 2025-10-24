import sys
input = sys.stdin.readline


N, K = map(int, input().split())

items = [] 

for _ in range(N):
    w, v = map(int,input().split())
    items.append((w,v))
    
DP = [0] * (K+1)

for item in items:
    if item[0] > K:
        continue
    for can_weight in range(K, item[0] -1 , -1):
        DP[can_weight] = max(DP[can_weight], DP[can_weight-item[0]] + item[1])
        
print(DP[K])