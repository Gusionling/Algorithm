import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = []
INF = 1e9

for _ in range(m):
    a,b,c = map(int, input().split())
    heapq.heappush(bus, (c,a,b))

board = [[INF] * n for _ in range(n)]

while bus:
    c,a,b = heapq.heappop(bus)
    #print(f'a:{a}, b:{b}, c:{c}')

    if c < board[a-1][b-1]:
        board[a-1][b-1] = c

        for i in range(n):
            if board[i][a-1] + board[a-1][b-1] < board[i][b-1]:
                if i == b-1:
                    continue
                board[i][b-1] = board[i][a-1] + board[a-1][b-1]
            if board[a-1][b-1] + board[b-1][i] < board[a-1][i]:
                if a-1 == i:
                    continue
                board[a-1][i] = board[a-1][b-1] + board[b-1][i]
            for j in range(n):
                if i == j:
                    continue
                board[i][j] = min(board[i][j] ,board[i][a-1] + c + board[b-1][j])
        
                

for i in range(n):
    for j in range(n):
        if board[i][j] == INF:
            board[i][j] = 0

for row in board:
    print(" ".join(map(str,row)))

