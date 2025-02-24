import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    # root가 아니라면
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA

n,m = map(int, input().split())
parent = list(range(n + 1))

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:  # Union 연산
        union(a, b)
    elif op == 1:  # Find 연산
        print("YES" if find(a) == find(b) else "NO")

