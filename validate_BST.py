import math

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isValidBST(root):
    return isValidBSTHelper(root, float('-inf'), float('inf'))

def isValidBSTHelper(node, min_val, max_val):
    if node is None:
        return True

    if not (min_val < node.val < max_val):
        return False

    left_is_valid = isValidBSTHelper(node.left, min_val, node.val)
    right_is_valid = isValidBSTHelper(node.right, node.val, max_val)

    return left_is_valid and right_is_valid

def buildTree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    return root

def buildInvalidTree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(18)
    root.right.right = TreeNode(20)
    return root

if __name__ == "__main__":
    print("Testing a valid BST:")
    root_valid = buildTree()
    if isValidBST(root_valid):
        print("The tree is a valid BST.")
    else:
        print("The tree is NOT a valid BST.")

    print("\nTesting an invalid BST:")
    root_invalid = buildInvalidTree()
    if isValidBST(root_invalid):
        print("The tree is a valid BST.")
    else:
        print("The tree is NOT a valid BST.")
