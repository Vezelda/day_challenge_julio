class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Insertamos los elementos en el BST
root = None
for key in [10, 5, 15, 2, 7]:
    root = insert(root, key)

# Recorrido inorder para verificar los elementos
print("Inorder traversal of the BST:")
inorder(root)
