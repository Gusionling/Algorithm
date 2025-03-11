import sys

input = sys.stdin.readline

S = input().strip()
unique_set  = set()

#i는 길이이다. 
for i in range(1, len(S)+1):
    for j in range(len(S) - i+1):
        pre_string = S[j:j+i]
        unique_set.add(pre_string)

print(len(unique_set))