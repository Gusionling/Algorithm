def z_visit(n, r, c):
    if n == 0:  # 기저 사례: 2^0 = 1 크기의 배열
        return 0
    half = 2 ** (n - 1)  # 현재 배열의 절반 크기
    if r < half and c < half:  # 1번 사분면
        return z_visit(n - 1, r, c)
    elif r < half and c >= half:  # 2번 사분면
        return half * half + z_visit(n - 1, r, c - half)
    elif r >= half and c < half:  # 3번 사분면
        return 2 * half * half + z_visit(n - 1, r - half, c)
    else:  # 4번 사분면
        return 3 * half * half + z_visit(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
print(z_visit(N, r, c))