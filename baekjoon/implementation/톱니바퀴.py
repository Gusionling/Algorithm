import sys
input = sys.stdin.readline

# 톱니바퀴 입력 받기
cycle = []
for _ in range(4):
    cycle.append(list(map(int, input().strip())))

# 포인터 인덱스 배열 (12시 방향 초기화)
pointers = [0 for _ in range(4)]

K = int(input())  # 회전 횟수

for _ in range(K):
    which, dir = map(int, input().split())
    which -= 1  # 인덱스 보정

    # 회전 여부와 방향 관리
    is_cycled = [0] * 4
    is_cycled[which] = dir

    # 오른쪽 전파
    for i in range(which, 3):
        if cycle[i][(pointers[i] + 2) % 8] != cycle[i+1][(pointers[i+1] + 6) % 8]:
            is_cycled[i+1] = -is_cycled[i]  # 반대 방향으로 회전
        else:
            break

    # 왼쪽 전파
    for i in range(which, 0, -1):
        if cycle[i][(pointers[i] + 6) % 8] != cycle[i-1][(pointers[i-1] + 2) % 8]:
            is_cycled[i-1] = -is_cycled[i]  # 반대 방향으로 회전
        else:
            break

    # 실제 회전 수행
    for i in range(4):
        if is_cycled[i] != 0:
            if is_cycled[i] == 1:
                pointers[i] = (pointers[i] - 1) % 8  # 시계 방향
            else:
                pointers[i] = (pointers[i] + 1) % 8  # 반시계 방향

# 최종 점수 계산
score = 0
for i in range(4):
    score += cycle[i][pointers[i]] * (2 ** i)

print(score)