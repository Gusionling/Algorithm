import sys, heapq

input = sys.stdin.readline

max_heap = []  # (-난이도, -문제번호)
min_heap = []  # (난이도, 문제번호)
problems = {}  # 문제번호 -> 현재 난이도 매핑

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(max_heap, (-L, -P))
    heapq.heappush(min_heap, (L, P))
    problems[P] = L

M = int(input())
for _ in range(M):
    order = input().split()

    if order[0] == 'recommend':
        if order[1] == '1':
            # 힙 상단이 유효한지 확인 (문제가 존재하고 난이도가 일치하는지)
            while max_heap:
                L, P = max_heap[0]
                L, P = -L, -P
                if P in problems and problems[P] == L:
                    print(P)
                    break
                heapq.heappop(max_heap)
        else:
            while min_heap:
                L, P = min_heap[0]
                if P in problems and problems[P] == L:
                    print(P)
                    break
                heapq.heappop(min_heap)
            
    elif order[0] == 'add':
        P, L = int(order[1]), int(order[2])
        heapq.heappush(max_heap, (-L, -P))
        heapq.heappush(min_heap, (L, P))
        problems[P] = L  # 현재 난이도 기록
        
    else:  # solved
        P = int(order[1])
        del problems[P]  # 딕셔너리에서 제거