def draw_triangle(n):
    # 2차원 배열로 전체 영역을 공백으로 초기화
    # 높이는 n, 너비는 2*n-1
    triangle = [[' '] * (2 * n - 1) for _ in range(n)]
    
    def fill_triangle(size, row, col):
        if size == 3:
            # 기저 사례: 가장 작은 삼각형 그리기
            triangle[row][col] = '*'
            triangle[row + 1][col - 1] = '*'
            triangle[row + 1][col + 1] = '*'
            for i in range(5):
                triangle[row + 2][col - 2 + i] = '*'
        else:
            # 재귀 사례: 3개의 작은 삼각형으로 분할
            half = size // 2
            
            # 위쪽 삼각형
            fill_triangle(half, row, col)
            
            # 아래쪽 왼쪽 삼각형
            fill_triangle(half, row + half, col - half)
            
            # 아래쪽 오른쪽 삼각형
            fill_triangle(half, row + half, col + half)
    
    # 최상단 중앙에서 시작
    fill_triangle(n, 0, n - 1)
    
    # 결과 출력
    for row in triangle:
        # 각 행의 끝 공백 제거
        print(''.join(row))

# 입력 받기
n = int(input())
draw_triangle(n)