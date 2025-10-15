import sys, heapq

input = sys.stdin.readline

list_B = []  # 최대 힙: (-L, -P)
list_S = []  # 최소 힙: (L, P)
solved = set()  # 해결된 문제 번호

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(list_B, (-L, -P))
    heapq.heappush(list_S, (L, P))

M = int(input())
for _ in range(M):
    order = input().split()

    if order[0] == 'recommend':
        if order[1] == '1':
            # 어려운 문제 (최대 힙)
            while list_B and -list_B[0][1] in solved:
                heapq.heappop(list_B)
            print(-list_B[0][1])
        else:
            # 쉬운 문제 (최소 힙)
            while list_S and list_S[0][1] in solved:
                heapq.heappop(list_S)
            print(list_S[0][1])
            
    elif order[0] == 'add':
        P, L = int(order[1]), int(order[2])
        heapq.heappush(list_B, (-L, -P))
        heapq.heappush(list_S, (L, P))
        
    else:  # solve
        P = int(order[1])
        solved.add(P)