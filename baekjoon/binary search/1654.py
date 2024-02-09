k, n = map(int, input().split())
straps = [int(input()) for _ in range(k)]

start =  1 
end = max(straps)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = sum(lan // mid for lan in straps)

    if count < n:
        end = mid -1
    else: 
        result = mid
        start = mid + 1

print(result)
