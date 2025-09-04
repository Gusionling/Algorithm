import sys

input = sys.stdin.readline

def oper1(array):
    # 상하 반전
    N = len(array)
    temp = []
    for i in range(N):
        temp.append(array[N-i-1])
    return temp

def oper2(array):
    # 좌우 반전
    temp = []
    for row in array:
        temp.append(list(reversed(row)))  # list()로 감싸기
    return temp

def oper3(array):
    # 오른쪽으로 90도 회전
    N, M = len(array), len(array[0])
    temp = [[0] * N for _ in range(M)]  # M x N 크기
    
    for i in range(N):
        for j in range(M):
            temp[j][N-1-i] = array[i][j]  # (i,j) -> (j, N-1-i)
    
    return temp

def oper4(array):
    # 왼쪽으로 90도 회전
    N, M = len(array), len(array[0])
    temp = [[0] * N for _ in range(M)]  # M x N 크기
    
    for i in range(N):
        for j in range(M):
            temp[M-1-j][i] = array[i][j]  # (i,j) -> (M-1-j, i)
    
    return temp

def oper5(array):
    # 4개 그룹을 시계방향으로 회전
    N, M = len(array), len(array[0])
    temp = [[0] * M for _ in range(N)]
    
    # 1그룹 -> 2그룹
    for i in range(N//2):
        for j in range(M//2):
            temp[i][j + M//2] = array[i][j]
    
    # 2그룹 -> 4그룹
    for i in range(N//2):
        for j in range(M//2, M):
            temp[i + N//2][j] = array[i][j]
    
    # 4그룹 -> 3그룹
    for i in range(N//2, N):
        for j in range(M//2, M):
            temp[i][j - M//2] = array[i][j]
    
    # 3그룹 -> 1그룹
    for i in range(N//2, N):
        for j in range(M//2):
            temp[i - N//2][j] = array[i][j]
    
    return temp

def oper6(array):
    # 4개 그룹을 반시계방향으로 회전
    N, M = len(array), len(array[0])
    temp = [[0] * M for _ in range(N)]
    
    # 1그룹 -> 3그룹
    for i in range(N//2):
        for j in range(M//2):
            temp[i + N//2][j] = array[i][j]
    
    # 3그룹 -> 4그룹
    for i in range(N//2, N):
        for j in range(M//2):
            temp[i][j + M//2] = array[i][j]
    
    # 4그룹 -> 2그룹
    for i in range(N//2, N):
        for j in range(M//2, M):
            temp[i - N//2][j] = array[i][j]
    
    # 2그룹 -> 1그룹
    for i in range(N//2):
        for j in range(M//2, M):
            temp[i][j - M//2] = array[i][j]
    
    return temp

N, M, R = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(map(int, input().split())))

operations = list(map(int, input().split()))

# 각 연산 수행
for op in operations:
    if op == 1:
        array = oper1(array)
    elif op == 2:
        array = oper2(array)
    elif op == 3:
        array = oper3(array)
    elif op == 4:
        array = oper4(array)
    elif op == 5:
        array = oper5(array)
    elif op == 6:
        array = oper6(array)

for row in array:
    print(' '.join(map(str, row)))