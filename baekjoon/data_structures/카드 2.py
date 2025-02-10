import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

#덱 초기화
for i in range(1,N+1):
    queue.append(i)

while len(queue) != 1:
    bye = queue.popleft()
    back = queue.popleft()
    queue.append(back)

print(queue[0])
