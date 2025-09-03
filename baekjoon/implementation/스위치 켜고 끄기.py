import sys

input = sys.stdin.readline

N = int(input())
switch = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    
    gender, Num = map(int, input().split())
    num = Num -1
    
    # 남자인 경우
    if gender == 1:
        for i in range(num, N, Num):
            switch[i] = (switch[i] + 1) % 2
        
    
    else:
        switch[num] = (switch[num] + 1) % 2
        
        for i in range(1, N//2):
            if num + i < N and 0<=num-i and switch[num + i] == switch[num - i]:
                switch[num + i] = (switch[num + i] + 1) % 2
                switch[num - i] = (switch[num - i] + 1) % 2
            else:
                break

for i in range(0, N, 20):
    print(*switch[i:i+20])
            