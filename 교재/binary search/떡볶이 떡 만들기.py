n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x -mid
    if total < m:
        end = mid -1
    
    #요구한 떡의 양보다 많을 떄 
    else:
        result = mid #최대한 덜 짤랐을 때가 정답이므로 여기에 정답 입력
        start = mid + 1

print(result)