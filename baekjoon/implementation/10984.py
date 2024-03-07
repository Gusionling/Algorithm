s = int(input())

for _ in range(s):
    gpa = 0
    count = 0
    num = int(input())
    for i in range(num):
        array = list(input().split(' '))
        count += int(array[0])
        gpa += int(array[0]) * float(array[1])
    
    print(count ,round(gpa/count, 1))

