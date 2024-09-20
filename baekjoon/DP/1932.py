import sys
input = sys.stdin.readline


n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for level in range(1,n):
    for col in range(level+1):
        if col == 0:
            arr[level][col] = arr[level][col] + arr[level-1][col]
        elif col == level:
            arr[level][col] = arr[level][col] + arr[level-1][col-1]
        else:
            arr[level][col] = arr[level][col] + max(arr[level-1][col-1], arr[level-1][col])

#마지막 줄에서 최대값 출력
print(max(arr[n-1]))
        
        
        


