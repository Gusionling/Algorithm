import sys
import heapq

input = sys.stdin.readline

def find_can(pre_need, visited):
    can_build = []
    for i in range(1, N+1):
        if not pre_need[i] and not visited[i]:
            can_build.append(i)
            visited[i] = True
    return can_build

def remove_complete(pre_need, idx):
    for i in range(1, N+1):
        if idx in pre_need[i]:
            pre_need[i].remove(idx)

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    pre_need = [[] for _ in range(N+1)]
    
    need_time = [0] + list(map(int, input().split()))  # 인덱스를 1부터 시작하기 위해 [0] 추가
    visited = [False] * (N+1)
    
    for _ in range(K):
        pre, next = map(int, input().split())
        pre_need[next].append(pre)
    
    # 목표 건물 번호 입력 받기 (문제에서 요구함)
    W = int(input())
    
    # build는 건물 지을 수 있는 것들
    build = find_can(pre_need, visited)
    
    complete_time = []
    
    time = 0
    
    while build:
        for start in build:
            heapq.heappush(complete_time, [time + need_time[start], start])
        
        build = []  # build 초기화
        
        time, idx = heapq.heappop(complete_time)
        
        remove_complete(pre_need, idx)
        
        # 목표 건물이 완성되었는지 확인
        if idx == W:
            break
        
        building = find_can(pre_need, visited)
        
        # 건설 가능한 건물이 없을 때 다음 완성 시간까지 기다림
        while not building and complete_time:
            time, idx = heapq.heappop(complete_time)
            remove_complete(pre_need, idx)
            
            # 목표 건물이 완성되었는지 확인
            if idx == W:
                break
                
            building = find_can(pre_need, visited)
        
        # 목표 건물이 완성되었는지 다시 확인
        if idx == W:
            break
            
        build.extend(building)  # extend로 리스트 요소들을 추가
    
    print(time)