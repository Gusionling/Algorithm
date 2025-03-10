import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def pow(b):
    if b == 1:
        return A % C
    
    #제곱수가 짝수라면 
    if b % 2 == 0:
        result = pow(b/2)
        return (result * result) % C
    else:
        result = pow(b//2)
        return (result * result * A ) % C
    
print(pow(B))
     