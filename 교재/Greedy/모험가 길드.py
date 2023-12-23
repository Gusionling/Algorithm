n = int(input())
data=list(map(int, input().split()))
data.sort()

groups=0
group=-1
size=0

for i in range(len(data)):
    if group ==-1:
        size = data[i]
        group = data[i]
        group -= 1
        if group == 0:
            groups += 1
            group = -1
            size = 0
    elif data[i] == size:
        group -= 1
        if group == 0:
            groups += 1
            group = -1
            size = 0
    elif data[i] > size:
        size = data[i]
        group = data[i] - group -1

print(groups)



    
    
