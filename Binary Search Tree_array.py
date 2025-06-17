import collections

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def main():
    try:
        num_elements = int(input("Enter number of elements: "))
        if num_elements < 0:
            print("Number of elements cannot be negative.")
            return

        print("Enter the elements (space-separated):")
        elements_str = input()
        arr = [int(x) for x in elements_str.split()]

        if len(arr) != num_elements:
            print(f"Warning: You entered {len(arr)} elements, but specified {num_elements}.")

        root = None
        for val in arr:
            root = insert(root, val)

        print("In-order Traversal of BST:")
        inorder(root)
        print() # For a newline at the end

    except ValueError:
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
