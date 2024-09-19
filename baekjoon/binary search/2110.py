# 가장 인접한 공유기 사이의 최대 거리이다. 
# 거리 기준 이분 탐색이 문제의 핵심이다. 
# 문제 답이 최소 거리니까 최소 거리를 key로 잡고 문제를 접근 
# key와 실제 값의 비교 (key가 진짜 나오는 값인지도 판별...? - 하지 않는 방법은?)
# 일단 key 값이 전체 길이를 c개 이상 낼 수 있어야 함
# 실제 값과 검증,,,, if 안되면? 더 작게 쪼개야지 key -1로 해서 쪼개는게 나을 듯 아니면 나온 key 값에 가장 근접한 값으로 ㄱㄱ 하던가
# 실제 값과 검증을 어떻게 하지...?

import sys
input = sys.stdin.readline

# input variables 
homes, routers = map(int, input().split())
distances = []
for i in range(homes):
    distances.append(int(input()))

# binary search setting
start = 0 
end = max(distances)

while(start <= end):
    mid = (start + end) // 2

    # max_counts divide total distance to check it can be use as answer
    max_counts = max // mid

    if max_counts < routers:
        end = mid
    else:
        # checking logic 




