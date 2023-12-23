n , k =map(int, input().split())

result = 0

while True:
    target = (n//k)*k
    #1을 빼주는 횟수
    result += (n- target)
    n = target
    if n<k:
        break
    result += 1
    n//=k

#마지막으로 남은 수에 대하여 1씩 빼기(1이 될 때까지)
result += (n-1) 
print(result)
