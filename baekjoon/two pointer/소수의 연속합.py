import sys
import math

N = int(input())

# 에라토스테네스의 체 초기화
prime = [True for i in range(N+1)]
primes = []

# 소수 찾기와 동시에 투 포인터 진행
result = 0
total = 0
left = 0

for p in range(2, N+1):
    # 이 숫자가 소수인지 확인
    if prime[p]:
        # p의 배수 제거
        for i in range(p*p, N+1, p):
            if i <= N:
                prime[i] = False
        
        # 소수 리스트에 추가
        primes.append(p)
        
        # 오른쪽 포인터에 새 소수 더하기
        total += p
        
        # 합이 N보다 크면 왼쪽 포인터 이동
        while total > N and left < len(primes)-1:
            total -= primes[left]
            left += 1
        
        # 합이 N과 같으면 결과 증가
        if total == N:
            result += 1

print(result)