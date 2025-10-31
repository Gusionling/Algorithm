import sys
input = sys.stdin.readline

N, M = map(int, input().split())
days = []
for _ in range(N):
    days.append(int(input()))

# 범위 설정
left = max(days)  # K는 최소한 하루 최대 금액 이상이어야 함
right = sum(days)  # 최악의 경우 전체 합

answer = right  # 초기화!

while left <= right:
    mid = (left + right) // 2
    
    count = 1  # 인출 횟수
    money = mid  # 처음 인출한 금액
    
    for day in days:
        if money < day:  # 현재 돈이 부족하면
            count += 1  # 재인출
            money = mid  # 새로 K원 인출
        
        money -= day  # 오늘 사용
    
    if count <= M:  # M번 이하로 가능
        answer = mid
        right = mid - 1  # 더 작은 K 시도
    else:  # M번 초과
        left = mid + 1  # K를 늘려야 함

print(answer)