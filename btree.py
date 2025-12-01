class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

root = Node(50)
root.left = Node(30)
root.right = Node(20)

def inorder_traverse(root):
    if root is not None:
        # print(root.data, end=" ")
        inorder_traverse(root.left)
        print(root.data, end=" ")
        inorder_traverse(root.right)
        # print(root.data, end=" ")


inorder_traverse(root)

