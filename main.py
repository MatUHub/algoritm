class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def search(node, val):
        if node is None or node.data == val:
            return node

        if node.data < val:
            return search(node.left, val)
        else:
            return search(node.right, val)

def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.data)
        print_tree(node.right)

root = Node(10)
node = search(root, 18)
if node:
    print(True)
else:
    print(False)
