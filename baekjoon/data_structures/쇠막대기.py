import sys
from collections import deque

imput = sys.stdin.readline

data = list(input().strip())
queue = deque()
cnt = 0
pre = '('

#스택에는 어차피 ) 는 들어가지 않는다. 처리할 뿐

for i in data:
    #레이저인지 판단
    if i == ')':
        # 레이저인 경우
        if pre == '(':
            queue.popleft()
            cnt += len(queue)
            pre = ')'

        else:
            queue.popleft()
            cnt += 1
            pre = ')'
    else:
        queue.append(i)
        pre = '('

print(cnt)