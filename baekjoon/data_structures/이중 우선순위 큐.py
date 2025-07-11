import sys
import heapq
from collections import Counter

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    k = int(input())
    
    min_heap = []    # 최소값용
    max_heap = []    # 최대값용 (음수 저장)
    counter = Counter()  # 원소 개수 추적
    
    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        
        if cmd == 'I':
            # 양쪽 힙에 모두 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            counter[num] += 1
            
        else:  # cmd == 'D'
            if not counter:
                continue
            
            if num == -1:  # 최솟값 삭제
                # 삭제된 원소들을 lazy하게 제거
                while min_heap and counter[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    counter[min_val] -= 1
                    if counter[min_val] == 0:
                        del counter[min_val]
                        
            else:  # 최댓값 삭제 (num == 1)
                # 삭제된 원소들을 lazy하게 제거
                while max_heap and counter[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    counter[max_val] -= 1
                    if counter[max_val] == 0:
                        del counter[max_val]
    
    # 최종 정리
    while min_heap and counter[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and counter[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    
    if not counter:
        print("EMPTY")
    else:
        print(f"{-max_heap[0]} {min_heap[0]}")