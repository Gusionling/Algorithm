import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
cctvs = []

for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((i, j, row[j]))

# CCTV별 방향 정의 (상: 0, 우: 1, 하: 2, 좌: 3)
directions = [
    [],  # 0번은 안쓰임
    [[0], [1], [2], [3]],  # 1번: 한 방향
    [[0, 2], [1, 3]],  # 2번: 양 반대편
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번: 직각
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번: 3방향
    [[0, 1, 2, 3]]  # 5번: 4방향
]

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

result = float('inf')

def mark(r, c, direction, board):
    """
    (r, c)에서 direction 방향으로 감시 표시
    변경된 좌표들을 반환
    """
    changed = []
    nr, nc = r + dr[direction], c + dc[direction]
    
    while 0 <= nr < N and 0 <= nc < M:
        if board[nr][nc] == 6:  # 벽이면 중단
            break
        if board[nr][nc] == 0:  # 빈 공간이면 표시
            board[nr][nc] = -1
            changed.append((nr, nc))
        nr += dr[direction]
        nc += dc[direction]
    
    return changed

def backtrack(depth, board):
    global result
    
    # 종료 조건: 모든 CCTV 처리 완료
    if depth == len(cctvs):
        # 사각지대 개수 세기
        blind_spot = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    blind_spot += 1
        result = min(result, blind_spot)
        return  # ← 여기서 return!
    
    r, c, cctv_type = cctvs[depth]
    
    # 현재 CCTV의 가능한 모든 방향 시도
    for dir_set in directions[cctv_type]:
        changed = []  # 이번 방향에서 변경된 좌표들
        
        # 선택: 각 방향으로 감시 표시
        for d in dir_set:
            changed.extend(mark(r, c, d, board))
        
        # 재귀: 다음 CCTV로
        backtrack(depth + 1, board)
        
        # 복원: 변경된 부분 되돌리기
        for cr, cc in changed:
            board[cr][cc] = 0

# 백트래킹 시작
backtrack(0, board)
print(result)