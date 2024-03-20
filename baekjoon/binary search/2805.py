n, h = map(int, input().split())
trees = list(map(int, input().split()))

def binaryS(trees):
    end = max(trees)
    start = 0
    result = 0
    
    while(start <= end):
        
        mid = (start + end) // 2
        #나무를 잘랐을 때 얻는 나무 길이의 합
        sum = 0

        for tree in trees:
            if tree > mid:
                sum += tree-mid
        
        if sum < h:
            end = mid - 1
        #필요한 나무길이보다 많을 때
        else:
            # h 이상의 나무 길이를 얻으면서 동시에 그 중 최대 높이를 찾기 위함이다. 
            result = mid
            start = mid + 1
    
    print(result)

binaryS(trees)
    
    

