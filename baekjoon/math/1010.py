t = int(input())
array = []


def combination(a, b):
    result = 1
    under = 1
    for i in range(b):
        result *= (a-i)
        under *= (b-i)
    print(result//under)

for _ in range(t):
    n, m = map(int, input().split())
    combination(m, n)

