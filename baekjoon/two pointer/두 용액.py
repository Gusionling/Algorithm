import sys

innput = sys.stdin.readline


N = int(input())
liquid = list(map(int, input().split()))

liquid.sort()

left = 0 
right = N-1
result = [liquid[left], liquid[right]]

ok = False
while left < right:
    
    sum_l = liquid[left] + liquid[right]
    # 갱신이 되는 경우
    if abs(sum_l) < abs(sum(result)):
        result = [liquid[left], liquid[right]]
    if sum_l < 0:
        left += 1
    elif sum_l == 0:
        print(liquid[left], liquid[right])
        ok = True
        break
    else:
        right -= 1
    
if ok == False:
    print(result[0],result[1]) 
            