import sys
input = sys.stdin.readline

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def multi_arr(a,b):
    
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j] % 1000
    
    return result

def square(x, n):
    if n == 1:
        return x
    temp = square(x, n//2)
    if n % 2 == 0:
        return multi_arr(temp, temp)
    else:
        return multi_arr(multi_arr(temp, temp), x)
    
result_arr = [[num % 1000 for num in row] for row in square(arr, B)]


for k in result_arr:
    print(*k)
    