import sys
sys.setrecursionlimit(10**8)
DP = {}
DP[0] =0
DP[1] = 1
DP[2] = 1

def dp(i):
    if i not in DP:
        if i%2 == 0:
            DP[i] = (dp(i//2) * (dp(i//2) + 2*dp(i//2-1))) % 1000000007
        else:
            DP[i] = (dp(i//2) * (dp(i//2)) + dp(i//2+1)**2) % 1000000007
    return DP[i]

n = int(input())

print(dp(n))