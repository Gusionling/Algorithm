n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d= [0]*(k+1)
# 딱 맞아 떨어지는 경우이다. 
d[0] = 1

for coin in array:
    for i in range(coin, k+1):
        d[i] += d[i - coin]

print(d[k])

        
            
