import sys
from collections import Counter

input = sys.stdin.readline

S, P = map(int, input().split())
origin_string = input().strip()
Ao, Co, Go, To = map(int, input().split())
total = 0

# Initialize counter for the first window
nums = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(P):
    char = origin_string[i]
    nums[char] += 1

# Check the first window
if nums['A'] >= Ao and nums['C'] >= Co and nums['G'] >= Go and nums['T'] >= To:
    total += 1

# Slide the window
for i in range(P, S):
    # Remove the character leaving the window
    nums[origin_string[i-P]] -= 1
    # Add the character entering the window
    nums[origin_string[i]] += 1
    
    # Check if the current window meets the criteria
    if nums['A'] >= Ao and nums['C'] >= Co and nums['G'] >= Go and nums['T'] >= To:
        total += 1

print(total)