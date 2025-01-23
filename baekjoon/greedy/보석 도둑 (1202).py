import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
dias = {}
for _ in range(N):
    print(" ")

bags = []
for _ in range(K):
    bags.append(int(input()))

# 작은 가방부터 얼른얼른 최대치로 배정
bags.sort()


