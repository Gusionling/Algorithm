import sys
from collections import deque

input = sys.stdin.readline

# 보드의 크기
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().strip()))

# 빨간 구슬, 파란 구슬, 구멍의 위치 찾기
rx, ry, bx, by, hx, hy = 0, 0, 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
        elif board[i][j] == 'O':
            hx, hy = i, j

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
def bfs():
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set([(rx, ry, bx, by)])
    
    while queue:
        crx, cry, cbx, cby, count = queue.popleft()
        
        # 10번 이상 움직였으면 실패
        if count >= 10:
            break
        
        for i in range(4):
            nrx, nry, nbx, nby = crx, cry, cbx, cby
            r_hole, b_hole = False, False
            
            # 빨간 구슬 이동
            while True:
                nrx += dx[i]
                nry += dy[i]
                
                if board[nrx][nry] == '#':  # 벽을 만나면
                    nrx -= dx[i]
                    nry -= dy[i]
                    break
                elif board[nrx][nry] == 'O':  # 구멍을 만나면
                    r_hole = True
                    break
                
            # 파란 구슬 이동
            while True:
                nbx += dx[i]
                nby += dy[i]
                
                if board[nbx][nby] == '#':  # 벽을 만나면
                    nbx -= dx[i]
                    nby -= dy[i]
                    break
                elif board[nbx][nby] == 'O':  # 구멍을 만나면
                    b_hole = True
                    break
            
            # 파란 구슬이 구멍에 빠지면 실패
            if b_hole:
                continue
                
            # 빨간 구슬만 구멍에 빠지면 성공
            if r_hole:
                return count + 1
            
            # 두 구슬이 같은 위치에 있으면 위치 조정
            if nrx == nbx and nry == nby:
                # 더 많이 이동한 구슬이 뒤로 한 칸
                r_dist = abs(nrx - crx) + abs(nry - cry)
                b_dist = abs(nbx - cbx) + abs(nby - cby)
                
                if r_dist > b_dist:  # 빨간 구슬이 더 많이 이동
                    nrx -= dx[i]
                    nry -= dy[i]
                else:  # 파란 구슬이 더 많이 이동
                    nbx -= dx[i]
                    nby -= dy[i]
            
            # 이미 방문한 상태면 건너뜀
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, count + 1))
    
    return -1  # 10번 이내에 성공하지 못하면 -1 반환

result = bfs()
print(result)