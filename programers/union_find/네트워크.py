def solution(n, computers):
    answer = 0
    
    parent = list(range(n))  # 더 간결한 초기화
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    def union(a, b):
        pa = find(a)
        pb = find(b)
        
        if pa != pb:
            parent[pb] = pa  # ✅ 루트끼리 연결
    
    # 연결 정보를 바탕으로 union
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                union(i, j)
    
    # 최종 경로 압축 (선택사항이지만 확실하게)
    for i in range(n):
        find(i)
    
    # 고유한 루트의 개수 = 네트워크 개수
    answer = len(set(parent))
    
    return answer