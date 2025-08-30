def matrix_multiply(A, B, mod):
    """2x2 행렬 곱셈"""
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]
    ]

def matrix_power(matrix, n, mod):
    """행렬의 n제곱을 빠른 거듭제곱으로 계산"""
    if n == 0:
        return [[1, 0], [0, 1]]  # 단위행렬
    
    result = [[1, 0], [0, 1]]  # 단위행렬로 초기화
    base = matrix
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        n //= 2
    
    return result

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    MOD = 1000000
    
    # 변환 행렬 [[1,1], [1,0]]
    A = [[1, 1], [1, 0]]
    
    # A^(n-1) 계산
    result_matrix = matrix_power(A, n-1, MOD)
    
    # [F(n), F(n-1)] = [F(1), F(0)] × A^(n-1) = [1, 0] × A^(n-1)
    # 따라서 F(n) = result_matrix[0][0] * 1 + result_matrix[0][1] * 0
    return result_matrix[0][0]

n = int(input())
print(fibonacci(n))