import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어 정보를 저장할 리스트 (r, c, s, d, z)
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r-1, c-1, s, d, z])  # 0-based 인덱스로 변환

def move_shark(r, c, s, d):
    """상어를 이동시키고 새로운 위치와 방향을 반환"""
    if d <= 2:  # 상하 이동
        # 상하 이동의 주기는 2*(R-1)
        if R == 1:
            return r, c, d
        
        cycle = 2 * (R - 1)
        s %= cycle
        
        if d == 1:  # 위쪽
            if s <= r:
                return r - s, c, d
            s -= r
            r = 0
            d = 2
            if s <= R - 1:
                return r + s, c, d
            s -= (R - 1)
            r = R - 1
            d = 1
            return r - s, c, d
        else:  # 아래쪽
            remain = R - 1 - r
            if s <= remain:
                return r + s, c, d
            s -= remain
            r = R - 1
            d = 1
            if s <= R - 1:
                return r - s, c, d
            s -= (R - 1)
            r = 0
            d = 2
            return r + s, c, d
    else:  # 좌우 이동
        # 좌우 이동의 주기는 2*(C-1)
        if C == 1:
            return r, c, d
        
        cycle = 2 * (C - 1)
        s %= cycle
        
        if d == 3:  # 오른쪽
            remain = C - 1 - c
            if s <= remain:
                return r, c + s, d
            s -= remain
            c = C - 1
            d = 4
            if s <= C - 1:
                return r, c - s, d
            s -= (C - 1)
            c = 0
            d = 3
            return r, c + s, d
        else:  # 왼쪽
            if s <= c:
                return r, c - s, d
            s -= c
            c = 0
            d = 3
            if s <= C - 1:
                return r, c + s, d
            s -= (C - 1)
            c = C - 1
            d = 4
            return r, c - s, d

result = 0

# 낚시왕이 각 열을 순회
for fisher_col in range(C):
    # 1. 낚시 - 현재 열에서 가장 위에 있는 상어를 잡기
    caught_shark = -1
    min_row = R
    
    for i, (r, c, s, d, z) in enumerate(sharks):
        if c == fisher_col and r < min_row:
            min_row = r
            caught_shark = i
    
    # 상어를 잡았다면 크기를 결과에 더하고 제거
    if caught_shark != -1:
        result += sharks[caught_shark][4]
        sharks.pop(caught_shark)
    
    # 2. 상어 이동
    for i in range(len(sharks)):
        r, c, s, d, z = sharks[i]
        new_r, new_c, new_d = move_shark(r, c, s, d)
        sharks[i] = [new_r, new_c, s, new_d, z]
    
    # 3. 상어끼리 싸움 - 같은 위치에 있는 상어들 중 가장 큰 것만 남기기
    position_map = {}
    
    for i, (r, c, s, d, z) in enumerate(sharks):
        pos = (r, c)
        if pos not in position_map:
            position_map[pos] = []
        position_map[pos].append(i)
    
    # 각 위치에서 가장 큰 상어만 남기기
    new_sharks = []
    for pos, shark_indices in position_map.items():
        if len(shark_indices) == 1:
            new_sharks.append(sharks[shark_indices[0]])
        else:
            # 크기가 가장 큰 상어 찾기
            max_size = 0
            best_shark = None
            for idx in shark_indices:
                if sharks[idx][4] > max_size:
                    max_size = sharks[idx][4]
                    best_shark = sharks[idx]
            new_sharks.append(best_shark)
    
    sharks = new_sharks

print(result)