n = int(input())
solution = list(map(int, input().split(' ')))

#정렬하기
solution.sort()

#이중포인터 설정
left = 0
right = n-1

answer = 2e+9+1
final = [] 

#투포인터
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
    
    if tot <0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])