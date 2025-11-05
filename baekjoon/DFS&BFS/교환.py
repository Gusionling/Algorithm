from collections import defaultdict

def solve():
    N, K = input().split()
    K = int(K)
    
    visited = defaultdict(set)
    visited[0].add(N)
    
    for step in range(K):
        for num in visited[step]:
            # 모든 (i, j) 교환 시도
            for i in range(len(num)):
                for j in range(i + 1, len(num)):
                    num_list = list(num)
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    next_num = ''.join(num_list)
                    
                    if next_num[0] != '0':
                        visited[step + 1].add(next_num)
    
    if not visited[K]:
        print(-1)
    else:
        print(max(map(int, visited[K])))

solve()
