t = int(input())
tests = []
for _ in range(t):
    tests.append(int(input()))

d0 = [0]*41
d1 = [0]*41

d0[0] = 1
d1[0] = 0
d0[1] = 0
d1[1] = 1

for i in range(t):
    for j in range(2, tests[i]+1):
        d0[j] = d0[j-1] + d0[j-2]
        d1[j] = d1[j-1] + d1[j-2]
    print(d0[tests[i]], d1[tests[i]])


