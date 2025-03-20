import sys
input = sys.stdin.readline

N = int(input())         # 패턴 P_N의 길이 (IOI 패턴의 반복 횟수)
S = int(input())         # 문자열 S의 길이
string = input().strip() # 입력 문자열

result = 0
pattern_count = 0
i = 1  # 인덱스 1부터 시작하여 3글자씩 확인

# 문자열을 순회하며 각 3글자 패턴 확인 (슬라이싱 없이)
while i < S - 1:
    # 현재 위치에서 "IOI" 패턴이 있는지 확인
    if string[i-1] == 'I' and string[i] == 'O' and string[i+1] == 'I':
        pattern_count += 1
        i += 2  # 다음 가능한 패턴으로 이동
        
        # N개의 연속된 "IOI" 패턴을 찾았을 때
        if pattern_count == N:
            result += 1
            # 패턴 카운트를 완전히 리셋하지 않고 1만 감소
            # 이렇게 하면 중첩된 패턴도 처리 가능
            pattern_count -= 1
    else:
        # 패턴이 깨지면 카운터를 리셋하고 한 위치 이동
        pattern_count = 0
        i += 1

print(result)