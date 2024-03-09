n = int(input())
people = list(map(int, input().split()))

people.sort()

times = 0
last = 0
for i in people:
    times += last + i
    last += i


print(times)

