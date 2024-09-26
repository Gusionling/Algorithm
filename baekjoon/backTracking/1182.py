import sys
input = sys.stdin.readline


N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

def backTracking(idx):
    global count
    if sum(box) == S and len(box) >0:
        count = count + 1

    for i in range(idx, N):
        box.append(nums[i])
        backTracking(i+1)
        box.pop()
        

box = []
backTracking(0)
print(count)