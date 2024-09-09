import sys

input = sys.stdin.readline

n = int(input())

#미리 첫 4개의 값을 리스트에 넣어두고 시작
P = [1,1,1,2,2]


for i in range(5, 99):
        P.append(P[i-1] + P[i-5])

for t in range(n):
    t = int(input())
    print(P[t-1])
