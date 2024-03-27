import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y]
  #심플하게 생각해라 
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return

#단색인 친구는 여기로 들어오게 된다. 
  if color == 0 :
    result.append(0)
  else:
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))