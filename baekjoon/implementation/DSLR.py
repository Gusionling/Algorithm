import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def D(current):
    return (current * 2) % 10000

def S(current):
    if current == 0:
        return 9999
    else:
        return current - 1

def L(current):
    # 왼쪽으로 순환: 1234 → 2341
    return (current % 1000) * 10 + current // 1000

def R(current):
    # 오른쪽으로 순환: 1234 → 4123
    return (current % 10) * 1000 + current // 10

for _ in range(T):
    start, target = map(int, input().split())
    
    if start == target:
        print("")
        continue
    
    visited = set()
    parent = {}
    operation = {}
    
    queue = deque([start])
    visited.add(start)
    parent[start] = -1
    
    found = False
    
    while queue and not found:
        current = queue.popleft()
        
        # D, S, L, R 연산 수행
        operations = [
            (D(current), 'D'),
            (S(current), 'S'),
            (L(current), 'L'),
            (R(current), 'R')
        ]
        
        for next_val, op in operations:
            if next_val not in visited:
                visited.add(next_val)
                parent[next_val] = current
                operation[next_val] = op
                queue.append(next_val)
                
                if next_val == target:
                    found = True
                    break
    
    # 경로 역추적
    result = []
    curr = target
    while parent[curr] != -1:
        result.append(operation[curr])
        curr = parent[curr]
    
    result.reverse()
    print(''.join(result))