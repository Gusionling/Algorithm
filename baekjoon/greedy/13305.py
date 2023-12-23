n = int(input())
length = list(map(int, input().split()))
oil= list(map(int, input().split()))
cost = 0
i = 0

#순회 위치를 맘대로 변경하기 위해서 for문 보다 while문 사용 
while i < n-1:
    
    cost += oil[i]*length[i]
    j = i + 1

    #남은 도시 중에 나보다 싼 도시까지 갈 거리 주유
    while j <n-1 and oil[i] < oil[j]:
        cost += oil[i] * length[j]
        j = j+1
    
    i = j

print(cost)


