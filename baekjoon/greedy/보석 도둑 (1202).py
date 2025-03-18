import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
gems = []
for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gems, (weight, value))

print(f'처음 보석들 : {gems}')
print(f'===================================')

# 가방을 오름차순 정렬
bags = [int(input()) for _ in range(K)]
bags.sort()
print(f'bags = {bags}')

total = 0
possible_gems = []  # 현재 가방에 넣을 수 있는 보석들 (가치 기준 최대 힙)

for bag in bags:
    # 현재 가방에 넣을 수 있는 모든 보석을 possible_gems에 추가
    while gems and gems[0][0] <= bag:
        weight, value = heapq.heappop(gems)
        # 최대 힙으로 저장 (가치가 큰 것부터 나오도록)
        heapq.heappush(possible_gems, (-value, weight))
        print(f'가방({bag})에 넣을 수 있는 보석 추가: weight={weight}, value={value}')
    
    # 가장 가치가 높은 보석을 선택
    if possible_gems:
        neg_value, weight = heapq.heappop(possible_gems)
        value = -neg_value  # 원래 값으로 변환
        total += value
        print(f'선택한 보석: weight={weight}, value={value}, 현재 가방={bag}')

print(total)