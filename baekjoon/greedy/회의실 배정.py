import sys

input = sys.stdin.readline

N = int(input())
arr = []
answer = 0

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : (x[1], x[0]))

end = 0
start = 0

for newStart, newEnd in arr:
    if newStart >= end:
        answer += 1 
        end = newEnd

print(answer)