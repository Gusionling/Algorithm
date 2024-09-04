import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [ i for i in range(n+1)]

array = list(map(int, input().split()))
known = array[1:]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootx = find(x)
    rooty = find(y)

    if rootx != rooty:
        #union을 하는 과정에서 
        #진실을 알고있는 집합의 원소가 부모가 될 수 있게
        if rootx in known:
            parent[rooty] = rootx
        elif rooty in known:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
    #서로 같은 집합에 속해 있는 경우        
    else:
        return


#union - find로 초기화 작업
parties = []
for i in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        union(party[i], party[i+1])
    
    parties.append(party)

ans = 0
for party in parties:
    for i in party:
        if find(i) in known:
            break
    else:
        ans += 1

print(ans)
        

