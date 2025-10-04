import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]

def check(r, c, st):
    """(r, c) 위치에 스티커를 붙일 수 있는지 확인"""
    n, m = len(st), len(st[0])
    if r + n > N or c + m > M:
        return False
    
    for i in range(n):
        for j in range(m):
            if st[i][j] == 1 and board[r+i][c+j] == 1:
                return False
    return True

def attach(r, c, st):
    """(r, c) 위치에 스티커 붙이기"""
    n, m = len(st), len(st[0])
    for i in range(n):
        for j in range(m):
            if st[i][j] == 1:
                board[r+i][c+j] = 1

def rotate(st):
    """시계방향 90도 회전"""
    r, c = len(st), len(st[0])
    rotated = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            rotated[j][r-1-i] = st[i][j]
    return rotated

for _ in range(K):
    n, m = map(int, input().split())
    sticker = []
    for i in range(n):
        row = list(map(int, input().split()))
        sticker.append(row)
    
    attached = False
    for deg in range(4):  # 4번 회전 시도
        if attached:
            break
        for i in range(N):  # 모든 위치 탐색
            for j in range(M):
                if check(i, j, sticker):
                    attach(i, j, sticker)
                    attached = True
                    break
            if attached:
                break
        sticker = rotate(sticker)

result = sum(sum(row) for row in board)
print(result)