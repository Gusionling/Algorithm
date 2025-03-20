import sys
from collections import Counter

input = sys.stdin.readline

N , d, k, c = map(int, input().split())
susies = []
for _ in range(N):
    susies.append(int(input()))

max_count = 0

for start in range(N):
    if start + k-1 >= N:
        select = susies[start:]
        diff = (start + k-1) - N 
        for i in range(diff+1):
            select.append(susies[i])
        #print(f"{diff+1}번째까지 더하긴 했습니다.")
    else:
        select = susies[start:start+k]
    
    count = len(set(select))
    #print(f'유니크 초밥 종류:{count}')
    if c not in select:
        count += 1
    max_count= max(max_count, count)

print(max_count)
    