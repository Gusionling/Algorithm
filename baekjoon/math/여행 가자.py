import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

parent = list( x for x in range(N+1) )


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b 


# 경로 압축 필요
def find(x):    
    if x != parent[x]:
        parent[x] =  find(parent[x])
    return parent[x]


for i in range(N):
    row = list(map(int,input().split()))

    for j in range(N):
        if row[j] == 1:
            union(i+1, j+1)
            
ways = list(map(int, input().split()))

for i in range(M-1):
    if find(ways[i]) != find(ways[i+1]):
        print('NO')
        exit()

print('YES')
                
        

