n,m = map(int, input().split())
money = list(map(int, input().split()))

max_val = 0
for st in range(n-(m-1)):
    max_val = max(max_val, sum(money[st:st+m]))
print(max_val)