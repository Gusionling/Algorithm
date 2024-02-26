
### 개념

- 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법이다. 
- **이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장**하여 다시 계산하지 않도록 한다. 
- 두 가지 방식으로 구성이 된다. 
	- top down
	- bottom up
- 일반적인 프로그램밍에서 사용하는 동적의 의미와 다르다. 

##### 조건
1. 최적 부분 구조(Optimal Substructure)
	- 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다. 
2. 중복되는 문제(Overlapping Subproblem)
	- 동일한 작은 문제를 반복적으로 해결해야한다. 
	- 재귀적으로 해결을 시도한다면 시간 복잡도가 비약적으로 상승할 수 있다. 

==점화식== 같은 경우?
- 피보나치
![[Pasted image 20240222130545.png]]

- f(2)가 반복적으로 호출되고 있는 것을 볼 수 있다. ==중복되는 부분 문제
	- 이와 같이 이미 해결한 문제들이 있다 (답을 알아서 다시 계산 안해도 되는 작은 문제들...)
	- 어딘가에 답을 저장해 두어야 한다. 

### 방식

##### 하향식 (Top Down)
**Memoization**
- 한 번 계산한 결과를 메모리 공간에 메모하는 기법이다. (전형적인 형태이다)
	- 같은 문제를 다시 호출하면 메모했던 결과를 가져온다.
	- 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 한다. 
- 결과 저장용 리스트는 DP 테이블이라고도 부른다. (최적인 친구들을 저장해 두는 곳이라고 이해하면 될 것 같다)
- Fibonaci 에서 
	- 기존에는 되게 오랜 시간 복잡도가 걸렸었다. 
	- Memozation 기법을 사용하면 상수시간에 해결이 가능하다. 
- 문제점
	- 오버헤드 : 재귀 호출의 오버헤드가 있을 수 있다. 
	- 스택 오버 플로우 : 깊은 재귀로 인해 스택오버플로우를 일으킬 위첨이 있다. 

```python
def fibonacci_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

# 예시 사용
n = 10
print(f"Top-Down: Fibonacci of {n} is {fibonacci_top_down(n)}")

```


##### 상향식 (Bottom Up)

- 반복적인 접근 방식을 사용하여 문제를 해결한다. 가장 작은 하위 문제부터 시작하여 답을 구축해 나가며, 이 과정에서 각 하위 문제의 결과를 테이블에 저장한다. 
- 하위 문제를 순차적으로 해결하며 최종 결과에 도달한다. 
```python
def fibonacci_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)
    return memo[n]

# 예시 사용
n = 10
print(f"Top-Down: Fibonacci of {n} is {fibonacci_top_down(n)}")

```


**피보나치(top down)**
```python
d = [0] * 100

def fibo(x):

    print('f('+ str(x) + ')', end=' ')

    if x == 1 or x == 2:

        return 1

    if d[x] != 0:

        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)

    return d[x]


fibo(6)
```


**다이나믹 프로그래밍 vs 분할 정복**
- 둘 다 최적 부분 구조를 가질 때 사용할 수 있다. 
- **차이점** : ==부분 문제의 중복==이다. 
	- DP 에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복이 된다. 
	- 분할 정복은 동일한 부분 문제가 반복적으로 계산되지 않는다. 

>[!abstract] 행동영역
> 1. 유형을 먼저 파악하는 것이 중요하다. 
> 2. 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토한다. 
> 3. 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 ==작은 문제에서 구현한 값이 문제에서 그대로 사용될 수 있으면== 코드를 개선하는 방법을 사용할 수 있다. 

### 문제

##### 문제 1 <개미 전사>
![[Pasted image 20240222172227.png]]
![[Pasted image 20240222172318.png]]

- 사고
	- 그리디로 갈 수 있을까? => 갈 수 없다. 
	- 완전 탐색을 하기에는 너무 크다.
	- DP...? 그러면 분할이 되어야 하는데 어떻게 분할을 하면 되지?
-  DP
	- **최적의 해** : i번째 식량창고에 대해서 털지 안 털지의 여부를 결정하기 위해서는 
		1. 직전 창고를 털어서 현재 창고를 못 턴다
		2. 직전 창고를 털지 않아서 현재 창고를 턴다. 
		- 이 두 가지 경우만 존재하게 되는데 두 가지 모두 최적 해를 담고 있기 때문에 앞까지 신경을 쓰지 않아도 된다. 

```python
n = int(input())
storage = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100


#다이나믹 프로그래밍(Dynamic Programing) 진행 (Bottom Up)
d[0] = storage[0]
d[1] = max(storage[0] , storage[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + storage[i])

print(d[n-1])
```

>[!note]
>풀이를 보면 점화식을 만드는 느낌이다. 
>이게 문제 흐름만 따라가다 보면 DP인지 전혀 모르겠는데 DP처럼 만든 문제인 것 같다. 


##### 문제 2 <1로 만들기>

![[Pasted image 20240223103420.png]]
![[Pasted image 20240223103540.png]]
- 사고
	- 일단 딱 보기만 하면 거스름돈 주는 것처럼 그리디와 유사해 보인다. 하지만 26의 예시처럼 3으로 먼저 나누는 것이 아닌 1을 빼주는게 더 최소이기 때문에 그리디로 해결할 수 없다. 
	- DP 문제의 흐름을 생각해보면 확실하지 않게 나올 때가 많은데 이럴 때 일 수록 심플하게 생각하는 것이 중요한 것 같다. 
	- 이 문제 같은 경우는 흐름대로 차근차근 생각을 해보았다. 4, 5, 6, 7, 8....일 때 최적 부분 구조로 말이다. 새로운 수에 연산을 가한 후 어떤 값이 나왔을 때 그 값의 최적 해를 이전 연산에 대하면 되는 것이다. 
- DP
	![[Pasted image 20240223110722.png]]

```python
x = int(input())

d = [0] * 30001
  

for i in range(2, x + 1):

    #현재의 수에서 1을 빼는 경우

    d[i] = d[i-1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우

    if i % 2 == 0:

        d[i] = min(d[i], d[i//2] + 1)

    if i % 3 == 0:

        d[i] = min(d[i], d[i//3] +1)

    if i % 5 ==0:

        d[i] = min(d[i], d[i//5] +1)

  

print(d[x])
```

>[!note]
>DP는 DP 테이블을 위주로 코드가 짜여진다는 것을 놓치지 말자


##### 문제 3 <효율적인 화폐 구성>
![[Pasted image 20240223115749.png]]
![[Pasted image 20240223115811.png]]

- 사고
	![[Pasted image 20240223125036.png]]
```python
n, m = map(int, input().split())

list = []

for _ in range(n):

    list.appen(int(input()))

  

d = [10001]*(m+1)

d[0] = 0

for i in range(n):

    for j in range(list[j], m+1):

        if d[j - list[i]] !=10001:

            d[j] = min(d[j], d[j-list[i]]+1)

  

if d[m] == 10001:

    print(-1)

else:

    print(d[m])

```
>[!note]
>한칸 한칸 나가는 것이 아니라 빼는 수 하나로 업데이트 싹 하고 그 다음 수로 넘어가서 업데이트하고 
>왜 이렇게 하냐? 일단 한칸 한칸 하면 시작을 어디부터 해야하는지가 문제다 뺐을 때 인덱스 범위를 너머가버릴 수 있음 그렇기에 처음부터 빼는 수가 필요하다 코드를 보면 이해가 될 것 이다. 


##### 문제 4 < 금광>
![[Pasted image 20240225173208.png]]
![[Pasted image 20240225173327.png]]
- 사고
	- 이 문제도 처음 봤을 때 그리디 아니야? 라고 생각이 될 수 있지만 아니다 
	- 3가지 밖에 선택지가 없기 때문에 길을 한번 들어버리면 더 큰 메리트의 길을 가지 못할 수도 있다. 
	- 와 씨... 나는 현재 위치에서 3가지로 가는 것 밖에 생각을 못했다. (시간 복잡도 n^m) 
	- 현재 위치는 3가지 경우에서 온다라는 것이 해결 아이디어였다. (n * m)
	![[Pasted image 20240225180503.png]]
```python
#테스트 케이스 입력
for tc in range(int(input())):
    #금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    #다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp=[]
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    #다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left, left_down, left_up)
    #가장 오른쪽 열 중에서 가장 큰 값을 선택하자
    result = 0
    for i in range(n):
        result = max(result , dp[i][m-1])
    print(result)
```
>[!note]
>"이런 식으로 입력을 처리할 수도 있구나"라는 것을 알게 되었다.



##### 문제 5 <병사 배치하기>

![[Pasted image 20240226145920.png]]
![[Pasted image 20240226145944.png]]![[Pasted image 20240226150013.png]]
- 사고 
	- 진짜 Dp 어렵다 어려워.... 
	- 그냥 보면 완전 탐색인데....왜 dp를 써야할까? 
	- dp는 보통 그 때 내가할 수 있는 경우의 수가 정해져있어서 경우끼리 비교해서 선택하는 방식이였는데...
	- ![[Pasted image 20240226151916.png]]
	- ![[Pasted image 20240226152550.png]]


```python
n = int(input())
array = list(map(int, input().split()))
#순서를 뒤집어 '최장 즈가 부분 수열 문제로 변환'
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1]*n

#가장 긴 증가하는 부분 수열(LTS) 알고리즘 수행
for i in range(1, n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
```

>[!note]
>새로운 리스트를 하나 만들어서 값을 저장해둔다. 완전 탐색 느낌이 맞기는 하다. 
>이 문제는 유형을 잘 기억해두었다가 LIS로 풀 수 있겠구나라는 것을 인지 해두자 