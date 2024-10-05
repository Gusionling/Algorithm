import sys
input = sys.stdin.readline

n, m = map(int, input().split())
salary = list(map(int, input().split()))

salary.sort(reverse=True)

total = sum(salary[:m])
print(total)