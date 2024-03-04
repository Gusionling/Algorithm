cash = int(input())
stock = list(map(int, input().split(' ')))

def bnf(cash, list):
    
    money = cash
    num = 0
    for i in range(13):
        if cash >= list[i]:
            num += (money // list[i])
            money %= list[i]
    return money + num * list[13]

def timing(cash, list):
    money = cash
    num = 0
    up = 0
    down = 0
    for i in range(1, 13):
        if list[i] > list[i-1]:
            up += 1
            down = 0
        elif list[i] < list[i-1]:
            down += 1
            up = 0
        else:
            continue
        if down == 3:
            num += (money // list[i])
            money %= list[i]
            down = 0
        elif up == 3:
            money += num * list[i]
            num = 0
            up = 0
    return money + num * list[13]

if bnf(cash, stock) > timing(cash, stock):
    print("BNF")
elif bnf(cash, stock) < timing(cash, stock):
    print("TIMING")
else:
    print("SAMESAME")
            

