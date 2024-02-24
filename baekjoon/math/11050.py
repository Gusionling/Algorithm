n, k = map(int, input().split())

child = 1
parent = 1

for i in range(k):
    child *= (n - i)
    parent *= (k - i)

print(child // parent)
