def solve_lucas():

    MOD = 1000000007
    
    def small_binomial(n, k, p):
        if k > n:
            return 0
        if k == 0 or k == n:
            return 1
        
        numerator = 1
        denominator = 1
        
        for i in range(k):
            numerator = (numerator * (n - i)) % p
            denominator = (denominator * (i + 1)) % p
        
        return (numerator * pow(denominator, p - 2, p)) % p
    
    def lucas_theorem(n, k, p):
        if k > n:
            return 0
        
        result = 1
        while n > 0 or k > 0:
            n_digit = n % p
            k_digit = k % p
            
            result = (result * small_binomial(n_digit, k_digit, p)) % p
            
            n //= p
            k //= p
        
        return result
    
    N, K = map(int, input().split())
    print(lucas_theorem(N, K, MOD))

solve_lucas()  