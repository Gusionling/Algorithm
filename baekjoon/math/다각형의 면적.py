# 백준 2166번 - 다각형의 넓이
# Shoelace Formula(신발끈 공식) 사용

n = int(input())
points = []

# 좌표 입력 받기
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

# Shoelace Formula로 넓이 계산
def calculate_area(points):
    n = len(points)
    area = 0
    
    # Shoelace Formula: 1/2 * |Σ(x_i * y_{i+1} - x_{i+1} * y_i)|
    for i in range(n):
        j = (i + 1) % n  # 마지막 점에서 첫 번째 점으로 연결
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    
    return abs(area) / 2

# 결과 출력 (소수점 첫째 자리에서 반올림)
result = calculate_area(points)
print(f"{result:.1f}")