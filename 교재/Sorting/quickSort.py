array = [7,5,9,0,2,3,5,6,8]

def quick_sort(array, start, end):
    if start >= end : #원소가 1개인 경우 종료 
        return 
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left+=1

        while(right > start and array[right]>=array[pivot]):
            right -= 1
        if(left > right): # 엇갈 렸다면 작은 데이터와 피벗을 교체
            array[right] , array[pivot] = array[pivot] , array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left] , array[right] = array[right]. array[left]
        
    quick_sort(array, start, right -1)
    quick_sort(array, right + 1, end)
    
quick_sort(array, 0, len(array) -1)
print(array)
            