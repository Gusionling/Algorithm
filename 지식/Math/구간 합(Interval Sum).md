- 구간 합 문제 : 연속적으로 나열된 N개의 수가 있을 때 특정 구간의 모든 수를 합한 값을 계산하는 문제

**구간 합 빠르게 계산하기**
- 접두사 합(Prefix Sum) : 배열의 맨 앞부터 특정 위치까지의 합을 미리 구해 놓은 것
- N개의 수 위치 각각에 대하여 접두사 합을 계산하여 P에 저장한다. 
- 매 M개의 쿼리 정보를 화긴할 때 구간 합은 P[Right] - P[Left-1]이다. 

![[Pasted image 20240318143449.png]]

```python
#데이터 개수 N과 데이터 입력 받기
n = 5
data = [10, 20, 30, 40, 50]

#접두사 합(Prefix Sum) 배열 게산
sum_value = 0
prefix_sum = [0]
for i in data:
	sum_value += i
	prefix_sum.append(sum_value)

#구간 합 계산 (세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])


```

## 배열의 값이 자주 바뀔 때는...?
- 구간 합은 원래 배열이 잘 바뀌지 않을 때 사용하는 것이 좋다. (당연하다)
	- 바뀔 때마다 update를 해야되기 때문이다 
- 배열의 값이 자주 바뀔 때 사용되는 알고리즘이 바로
	- 세그먼트 트리 (인덱스 트리이다.)
	- 