import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input().strip()               # 수행할 함수
    n = int(input())                     # 배열의 길이
    arr = input().strip()                # 배열 입력

    # 배열 초기화    
    if n == 0:
        queue = deque()                  # 빈 배열 처리
    else:
        queue = deque(map(int, arr[1:-1].split(',')))  # 대괄호 제거 후 리스트 변환

    reverse_flag = False                 # 뒤집기 여부 플래그
    error_flag = False                   # 에러 발생 여부 플래그

    for command in func:
        if command == 'R':
            reverse_flag = not reverse_flag  # 뒤집기 상태 토글
        elif command == 'D':
            if not queue:
                print("error")               # 빈 큐에서 삭제 시 에러 출력
                error_flag = True
                break
            if reverse_flag:
                queue.pop()                  # 뒤집힌 경우 뒤에서 삭제
            else:
                queue.popleft()              # 정상 상태일 때 앞에서 삭제

    # 정상적인 경우 출력 처리
    if not error_flag:
        if reverse_flag:
            queue.reverse()                 # 최종 뒤집기 적용 (효율적)
        print(f"[{','.join(map(str, queue))}]")