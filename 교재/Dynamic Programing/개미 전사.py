n = int(input())
storage = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

#다이나믹 프로그래밍(Dynamic Programing) 진행 (Bottom Up)
d[0] = storage[0]
d[1] = max(storage[0] , storage[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + storage[i])


print(d[n-1])