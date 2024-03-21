import heapq
import sys

input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    num = int(input())
    if num == 0:
        #우선 순위 큐가 비어있을 경우
        if not q:
            print(0)
        else:
            ab, real = heapq.heappop(q)
            print(real)
    else:
        #튜플 형태로 저장
        #heapq는 첫번째 요소를 기준으로 정렬을 하고 필요한 경우 다음 요소를 기준으로 정렬 
        heapq.heappush(q, (abs(num), num))
        #절대값이 같을 떄는 큰 수부터 내보내고 싶다하면
        #heapq.heappush(q, (abs(num), -num))하면되고 출력할 떄 -num하면 된다. 
