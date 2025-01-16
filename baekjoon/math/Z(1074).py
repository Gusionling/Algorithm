import sys

imput = sys.stdin.readline

N, r, c = map(int, input().split())
location = pow(2, N) * (r+1) + c+1
answer = 0

def divide(n, l):
    
    global answer

    if n == 1:
        answer += l
        return
    
    size = pow(4, n)
    hole = size // l

    answer += hole * pow(4, n-1)


    divide(n-1, size % l)

divide(N,location)

print(answer)

    
    

