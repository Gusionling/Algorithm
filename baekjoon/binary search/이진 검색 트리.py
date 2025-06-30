import sys
sys.setrecursionlimit(20000)  # 이 줄 추가!

def postorder(preorder):
    if len(preorder) == 0:
        return
    
    if len(preorder) == 1:
        print(preorder[0])
        return
    
    root = preorder[0]
    
    right_idx = 1
    while right_idx < len(preorder) and preorder[right_idx] < root:
        right_idx += 1
    
    postorder(preorder[1:right_idx])
    postorder(preorder[right_idx:])
    print(root)

preorder = [int(line.strip()) for line in sys.stdin]
postorder(preorder)