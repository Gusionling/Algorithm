#p.93 그리디 실전 문제 큰 수의 법칙
from sys import stdin as s

s=open("input.txt", "rt")

n, m, k = map(int, s.readline().split())
data = list(map(int, s.readline().split()))

#입력받은 수를 정렬하여 가장 큰 2개의 수만 뽑으면 된다. 
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while(True):
    for i in range(k):
        if m == 0:
            break
        m -= 1
        result += first
    if m == 0:
        break
    result += second
    m -= 1

print(result)

