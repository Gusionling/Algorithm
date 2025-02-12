import sys

input = sys.stdin.readline

n, m = map(int, input().split())
salary = list(map(int,input().split()))

sum = 0
for i in range(m):
    sum += salary[i]
max_sum = sum

for i in range(m, n):
    sum = sum + salary[i] - salary[i-m]
    max_sum = max(max_sum, sum)
    
print(max_sum)
