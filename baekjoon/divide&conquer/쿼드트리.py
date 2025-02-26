import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]

def compress(x, y, size):
    # 영역이 모두 같은 값인지 확인
    check = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != check:
                # 다른 값이 있으면 4분할하여 재귀 호출
                half = size // 2
                return '(' + compress(x, y, half) + \
                       compress(x, y + half, half) + \
                       compress(x + half, y, half) + \
                       compress(x + half, y + half, half) + ')'
    
    # 모두 동일한 값이면 그 값만 반환
    return str(check)

result = compress(0, 0, N)
print(result)