import sys

input = sys.stdin.readline

A, B = map(int, input().split())
count = 1
can = True
while A < B:
    
    # B가 짝수라면
    if B % 2 == 0:
        B = B / 2
        count += 1
    
    # B가 홀수라면
    else:
        if B % 10 == 1:
            B = B // 10
            count += 1
        else:
            can = False
            break

if can and A == B:
    print(count)
else:
    print(-1)