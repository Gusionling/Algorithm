import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))
remain = [w] * n

time = 1
now_weight = 0 
c_index = 0

while c_index < n:
    time += 1
    
    # 다리를 건널 수 있다면
    if now_weight + trucks[c_index] <= L:
        now_weight += trucks[c_index]
        c_index += 1
    
    for i in range(c_index):
        if remain[i] > 0:
            remain[i] -= 1
            if remain[i] == 0:
                now_weight -= trucks[i]
time += remain[-1]
    
print(time)