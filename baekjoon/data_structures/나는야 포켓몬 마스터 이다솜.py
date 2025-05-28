n, m = map(int, input().split())

# 두 개의 딕셔너리 사용
name_to_num = {}  # 이름 -> 번호
num_to_name = {}  # 번호 -> 이름

# 포켓몬 정보 입력
for i in range(1, n + 1):
    name = input().strip()
    name_to_num[name] = i
    num_to_name[i] = name

# 쿼리 처리
for _ in range(m):
    query = input().strip()
    if query.isdigit():
        # 숫자면 번호 -> 이름
        print(num_to_name[int(query)])
    else:
        # 문자면 이름 -> 번호
        print(name_to_num[query])