import sys
input = sys.stdin.readline

N = int(input())
# list archiving for answer's cases
answer = []
count = 0


def backTracking(row):
    global count
    #정답 검증로직
    if row == N:
        count = count + 1
        return     


    for col in range(N):
        if check(row, col, answer) == False:
            continue
        answer.append([row, col])
        backTracking(row+1)
        answer.pop()



def check(row, col, arr):
    # 이렇게 뽑을 수 있더라
    for r, c in arr:
       if c == col or abs(r-row) == abs(c - col):
           return False
    return True


backTracking(0)
print(count)