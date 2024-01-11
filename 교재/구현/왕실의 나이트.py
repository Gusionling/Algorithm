input_data = input()
x = int(ord(input_data[0])) - int(ord('a')) + 1
y = int(input_data[1])

dx=[-2,-2, -1, 1, 2, 2, -1, 1]
dy=[-1, 1, 2, 2, -1, 1, -2,-2]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny >8:
        continue
    count += 1

print(count) 
    

