#bfs로 풀어도 될 문제이지만 union Find로 풀어보고 싶었다. 
import sys 

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
size = [ 1 for _ in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx != rooty:
        if size[rootx] >= size[rooty]:
            parent[rooty] = rootx
            size[rootx] += size[rooty]
        else:
            parent[rootx] = rooty
            size[rooty] += size[rootx]
       

for i in range(m):
    start, end = map(int, input().split())
    union(start, end)

    
print(size[find(1)]-1)
