import sys, copy

input = sys.stdin.readline

'''
걸린 시간 37분

뭔가 그리디 , 최적화 문제처럼 보임, 파라메틱 서치는 아니고 왜냐하면 최대 치킨집의 개수는 M으로 정해져 있기 때문에 
그러면 완탐이거나 , 조합(비트마스킹) 이겠지

일단 생각나는 것은 비트 마스킹 -> 다 해보는거임 , 물론 백트래킹으로 구현을 해도 됨
백트래킹으로 치킨집을 하나씩 추가하고 다익스트라 업데이트 하는 것 처럼 업데이트 하는 방식으로 하는게 맞을 것 같은데
'''

'''
주의 할 점은 헹열은 1,1 부터 시작한다는 거임 0 부터 시작하면 안되나? 거리 계산시에 에러 발생할 수 있어서 그런 것 같음
그리드 상에서의 좌표만 row + 1, col + 1
'''

INF = float('inf')
answer = INF

# 필요한 변수들 부터 생각
homes = [] # 위치 저장 
chiken_store = [] # 위치 저장
grid = []

N, M = map(int, input().split())

# 그리드 정보 받기
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        # 집인경우
        if row[j] == 1:
            homes.append((i+1,j+1))
        # 치킨집인 경우
        elif row[j] == 2:
            chiken_store.append((i+1,j+1))
    
    grid.append(row)
    
chiken_nums = len(chiken_store)
home_nums = len(homes)
chiken_dist = [INF] * home_nums
            
# 선택된 치킨집을 어떻게 트래킹, 기록하지?
visited = [False] * chiken_nums

def back(depth, chiken_dist, visited, idx):
    
    if depth == M:
        global answer
        answer = min(answer, sum(chiken_dist))
        return
    
    if (depth + (chiken_nums-idx)) < M:
        return
    
    for i in range(idx, chiken_nums):
        if not visited[i]:
            visited[i] = True
            temp_dist = copy.deepcopy(chiken_dist)
            for j in range(home_nums):
                hr, hc = homes[j]
                row_dist = abs(hr - chiken_store[i][0])
                col_dist = abs(hc - chiken_store[i][1])
            
                if chiken_dist[j] > row_dist + col_dist:
                    chiken_dist[j] = row_dist + col_dist
            
            back(depth+1, chiken_dist, visited, i+1)
            # 복구하기
            chiken_dist = temp_dist
            visited[i] = False

back(0, chiken_dist, visited, 0)
print(answer)