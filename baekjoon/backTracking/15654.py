import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtracking(depth):
    if depth == M:
        print(' '.join(map(str,box)))
        return
    
    for i in range(N):
        if arr[i] in box:
            continue
        box.append(arr[i])
        backtracking(depth+1)
        box.pop()

box=[]
backtracking(0)




