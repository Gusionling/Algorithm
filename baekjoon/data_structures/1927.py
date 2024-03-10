import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
for i in range(n):
    num = int(input())
    if num == 0:
        #q가 비어있다면
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, num)

    