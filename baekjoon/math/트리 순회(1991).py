import sys
input = sys.stdin.readline

N = int(input())
tree = {}

# 트리를 딕셔너리로 구현
for _ in range(N):
    root, left, right = map(str, input().split())
    tree[root] = (left, right)

# 전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')  # 부모 출력
    preorder(tree[node][0])  # 왼쪽 자식
    preorder(tree[node][1])  # 오른쪽 자식

# 중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])  # 왼쪽 자식
    print(node, end='')  # 부모 출력
    inorder(tree[node][1])  # 오른쪽 자식

# 후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # 왼쪽 자식
    postorder(tree[node][1])  # 오른쪽 자식
    print(node, end='')  # 부모 출력

# 루트 노드는 항상 'A'로 시작
root = 'A'

# 각 순회를 호출
preorder(root)
print()  # 개행
inorder(root)
print()  # 개행
postorder(root)
print()  # 개행