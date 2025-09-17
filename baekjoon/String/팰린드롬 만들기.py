import sys
from collections import defaultdict

input = sys.stdin.readline

name = input().strip()

# 1. 팰린드롬을 만들고 2. 사전 순에서 가장 빠른걸로

chars = defaultdict(int)

for word in name:
    chars[word] += 1
    
count = 0
last = 'LAST'
result = []
for key, num in chars.items():
    if num % 2 != 0 and num != 1: 
        if count == 0:        
            count += 1
            last = key
        else:
            print("I'm Sorry Hansoo")
            exit()
    elif num == 1:
        if count == 0:        
            count += 1
            last = key 
        else:
            print("I'm Sorry Hansoo")
            exit()
        continue
        
    for _ in range(num//2):
        result.append(key) 

result.sort()                   
pre_result = result.copy()      # 정렬된 리스트 복사
last_result = result[::-1]      # 뒤집힌 리스트 생성
if last != 'LAST':
    pre_result.append(last)
fianl_result = pre_result + last_result

print(''.join(fianl_result))
    
    
    
        
    

