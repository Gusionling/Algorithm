n = 1260
count = 0

array=[500, 100, 50, 10]

for coin in array:
    count += n // coin #//은 정수 나눗셈 
    n %= coin

print(count)