import sys
import heapq

input = sys.stdin.readline
N = int(input())

left_heap = []   # 최대힙 (작은 절반)
right_heap = []  # 최소힙 (큰 절반)

for _ in range(N):
    num = int(input())
    
    # 1. 적절한 힙에 삽입
    if not left_heap or num <= -left_heap[0]:
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    
    # 2. 힙 크기 균형 맞추기
    if len(left_heap) > len(right_heap) + 1:
        # left가 너무 큼
        val = -heapq.heappop(left_heap)
        heapq.heappush(right_heap, val)
    elif len(right_heap) > len(left_heap):
        # right가 너무 큼
        val = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -val)
    
    # 3. 중간값 출력 (항상 left_heap의 최댓값)
    print(-left_heap[0])