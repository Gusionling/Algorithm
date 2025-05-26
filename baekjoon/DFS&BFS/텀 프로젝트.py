import sys
sys.setrecursionlimit(200000)

def find_cycles(n, choices):
    # 각 학생이 팀에 속하는지 여부
    in_team = [False] * (n + 1)
    # 방문 상태: 0(미방문), 1(방문중), 2(방문완료)
    visited = [0] * (n + 1)
    
    def dfs(student):
        if visited[student] == 1:  # 현재 경로에서 다시 만남 -> 사이클 발견
            # 사이클에 속한 모든 학생들을 팀으로 표시
            curr = student
            while True:
                in_team[curr] = True
                curr = choices[curr]
                if curr == student:
                    break
            return
        
        if visited[student] == 2:  # 이미 처리된 노드
            return
        
        visited[student] = 1  # 방문 중으로 표시
        dfs(choices[student])  # 다음 학생으로 이동
        visited[student] = 2  # 방문 완료로 표시
    
    # 모든 학생에 대해 DFS 수행
    for i in range(1, n + 1):
        if visited[i] == 0:
            dfs(i)
    
    # 팀에 속하지 않는 학생 수 계산
    return sum(1 for i in range(1, n + 1) if not in_team[i])

# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    n = int(input())
    choices_input = list(map(int, input().split()))
    
    # 1-indexed로 변환
    choices = [0] * (n + 1)
    for i in range(n):
        choices[i + 1] = choices_input[i]
    
    result = find_cycles(n, choices)
    print(result)