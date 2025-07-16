import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

ways = []
for _ in range(M):
    c1, c2, cost = map(int, input().split())
    heapq.heappush(ways, (cost, c1, c2))

parent = list(range(N+1))
num = N
total_cost = 0  # 간단하게 총 비용만 추적

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b, pay):
    global num, total_cost
    root_a = find(a)
    root_b = find(b)
    
    if root_a != root_b:
        parent[root_b] = root_a  # 간단하게
        total_cost += pay        # 비용 누적
        num -= 1
        return True
    return False

# 컴포넌트가 2개가 될 때까지만 union
while num > 2:
    pay, c1, c2 = heapq.heappop(ways)
    union(c1, c2, pay)

print(total_cost)