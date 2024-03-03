n = int(input())
drinks = list(map(int, input().split(' ')))

drinks.sort()
# 인덱스 -1은 끝에서 마지막 요소라는 뜻이다. -2는 끝에서 두번째 원소
total = drinks[-1]

for i in range(n-1):
    total += drinks[i]/2

print(total) 