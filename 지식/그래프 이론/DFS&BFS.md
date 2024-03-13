# 1. 스택과 자료구조
### (1) 스택 자료구조
- 선입선출 자료구조이다. 
- 삽입과 삭제의 동작으로 이루어진다. 
	- append( )와 pop( ) 메소드를 사용하면 된다. (ap 스택 쌓는다~)
	- 최상단 원소로부터 출력
	```python
		print(stack[::-1])
	```
	-  최하단 원소부터 출력
		```python 
		print(stack)
```

### (2) 큐 자료구조
- 선입선출 자료구조이다. 
- deque(덱) 라이브러리를 사용하자
	- from collections import deque
		- append( ) 와 popleft( )사용
		- reverse( )함수로 역순으로 바꿀 수 있다. 

# 2. 재귀함수

- 종료 조건을 넣어주어야 한다. 
- **유클리드 호제법**
	- 두 자연수에 대한 최대 공약수를 구하는 대표적인 알고리즘
		- 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자
		- 이때 A와 B의 최대 공약수는 B와 R의 최대 공약수와 같다. 
	```python
	def gcd(a, b):
		if a%b == 0:
			return b
		else:
			return gcd(b, a%b)
```

- ==재귀 함수 사용 시 유의 사함==
	- 재귀 함수를 활용하면 복잡한 알고리즘을 간결하게 할 수 있다. 
	- 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다. 
	- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다. 
	- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다. 

# 3. DFS (Depth - First Search)

- DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다. 
- DFS는 ==스택 자료구조(혹은 재귀 함수)==를 이용한다. 
- 백트래킹 느낌이다. 
- **동작과정**
		1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다. 
		2. 스택의 최상단 노드에 방문하지 않은 입접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않은 인접노드가 없으면 최상단 노드를 꺼낸다. 
		3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다. 

# 4. BFS( Breath-First Search)

- 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다. 
- ==큐 자료구조==를 이용한다. 
- **동작과정**
		1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다. 
		2. 큐에서 노드를 꺼낸 뒤에 해다 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다. 
		3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다. 


# 문제

### 음료수 얼려 먹기

![[Pasted image 20240312213825.png]]
![[Pasted image 20240312213900.png]]
```python
n, m = map(int, input().split())        

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def is_connect(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] == 1:
        return
		#이렇게 1로 바꿔주는 것은 좋은 것 같다. 통일성을 줄 수 있고 불필요한 연산을 줄인다 
    graph[x][y] = 1
    is_connect(x+1, y)
    is_connect(x-1, y)
    is_connect(x, y+1)
    is_connect(x, y-1)

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result += 1
            is_connect(i, j)

print(result)
```
>[!note]
>주어진 데이터에 변형을 가해 답을 구하는 문제

### 미로 탈출

![[Pasted image 20240312215609.png]]
![[Pasted image 20240312215652.png]]
```python
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input())))
dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
	queue = deque()
	queue.append((x,y))

	#큐가 빌 때까지 반복하기
	while queue:
		#방문 했으면 그 요소는 빠져야하는 것이고
		#빠진 요소는 인접한 요소가 추가 된다. 
		#queue에는 앞으로 방문할 요소들만 남게 된다. 빠질 때 처리할 것을 처리해주면 되는 것이다. 
		x, y = queue.popleft()
		#상하 좌우 표시
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if nx < 0 or nx >= n or ny <0 or ny >=m:
				continue
			#처음 방문하는 경우에만 최단 거리 기록
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx, ny))
	return graph[n-1][m-1]

print(bfs(0,0))
```

- 그래프를 담아둘 공간이 필요하고 
- 모든 지점에서의 기록이 필요하기 때문에 bfs사용 (뻗어나간다)