#마지막은 꼭 포함 시켜야 하기 때문에 마지막을 포함하는 것중에 최적의 해를 생각하면 된다. 
#DP라는 것을 보면 꼭 하나의 줄기에서 최적의 것을 선택하는 것이 아니다. 
#최적화 되고 있는 여러 줄기가 있을 수 있다. 

import sys

input = sys.stdin.readline

#이는 n이 301보다 작은 경우 리스트의 크기가 301보다 작아집니다. 
#이 경우, d[1] = stairs[1] + d[0] 또는 d[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1]) 같은 초기화 부분에서 인덱스 에러(IndexError)가 발생할 수 있습니다. 
# n = 1인경우 인덱스 에러가 발생한다. 

n = int(input())
stairs = [0] * 301
for i in range(n):
    stairs[i] = int(input())

d = [0]*301
#점화식을 보면 3단계 전까지는 봐야하기 때문에 d[3]까지 적어준다. 
d[0] = stairs[0]
d[1] = stairs[1] + d[0]
d[2] = max(stairs[2] + stairs[0] , stairs[2] + stairs[1])

for i in range(3, n):
    d[i] = max(stairs[i] + stairs[i-1] + d[i-3], stairs[i] + d[i-2])
    
print(d[n-1])