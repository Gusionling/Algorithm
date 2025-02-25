import sys
input = sys.stdin.readline

n = int(input().strip())  # 원소 개수
arr = list(map(int, input().split()))  # 입력 배열
visited = [False] * n  # 방문 체크
max_value = 0  # 최댓값 저장
current_permutation = []  # 현재 순열을 저장하는 리스트

# 백트래킹으로 순열 생성하면서 최댓값 찾기
def backtrack():
    global max_value
    
    # 순열이 완성되었을 때
    if len(current_permutation) == n:
        # 식 계산
        total = sum(abs(current_permutation[i] - current_permutation[i+1]) for i in range(n-1))
        max_value = max(max_value, total)
        return

    # 모든 숫자를 순열에 추가하면서 탐색
    for i in range(n):
        if not visited[i]:  # 아직 사용되지 않은 숫자라면
            visited[i] = True
            current_permutation.append(arr[i])

            backtrack()  # 재귀적으로 다음 숫자 선택

            # 원상복구 (백트래킹)
            visited[i] = False
            current_permutation.pop()

# 백트래킹 시작
backtrack()
print(max_value)