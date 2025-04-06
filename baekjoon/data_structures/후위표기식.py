import sys
from collections import deque

input = sys.stdin.readline

expr = list(input().strip())
answer = ""
stack = deque()

for cur in expr:
    if cur.isalpha():
        answer += cur
    elif cur == '(':
        stack.append(cur)
    elif cur == '*' or cur == '/':
        while stack and ( stack[-1] == '*' or stack[-1] == '/'):
            answer +=  stack.pop()
        stack.append(cur)
    elif cur == '+' or cur == '-':
        while stack and  stack[-1] != '(':
            answer += stack.pop()
        stack.append(cur)
    else:
        while stack and stack[-1] != '(':
            answer +=   stack.pop()
        stack.pop()
    
while stack:
    answer += stack.pop()
print(answer)

