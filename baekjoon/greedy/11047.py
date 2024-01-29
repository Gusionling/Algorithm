n , k = map(int , input().split())
coin_list = list()
for i in range(n):
    coin_list.append(int(input()))

count = 0
for coin in reversed(coin_list):
    count += k //coin
    k %= coin
    
print(count)