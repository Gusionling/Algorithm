import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
#Sorting numas
nums = sorted(set(nums))
box = []

#back traking function
def backTracking(depth, idx):
    global box
    
    # answer checking 
    if depth == M:
        print(" ".join(map(str, box)))
        return

    for i in range(idx, len(nums)):
        box.append(nums[i])
        backTracking(depth+1, i)
        box.pop()

backTracking(0, 0)






