import sys
import heapq

input= sys.stdin.readline

courses = []

N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(courses, (start, end))

time = 0
max_size = 0
room = []

# 원래 시간 단위로 while 문을 돌리려고 했으나 시간은 10의 9승이라 변경
while courses:
    s, e = heapq.heappop(courses)

    #쓰고 있는 강의실이 없다면
    if len(room)==0:
        heapq.heappush(room,e)
    #비교를 해야됨
    else:
        if s >= room[0]:
            heapq.heappop(room)
            heapq.heappush(room, e)
        else:
            heapq.heappush(room, e)

    is_max = len(room)

    max_size = max(max_size, is_max)

print(max_size)

