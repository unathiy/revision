# Define a class Node to represent the nodes in the binary tree
class Node:
def __init__(self, data):
self.data = data
self.left = None
self.right = None

# Define a recursive function to find the length of the binary tree
def tree_length(root):

# If the root is None, the length of the tree is 0
if root is None:
return 0
else:
# Recursively find the length of the left and right subtrees
left_subtree_length = tree_length(root.left)
right_subtree_length = tree_length(root.right)
# Return the length of the tree as 1 plus the maximum length of the left and right subtrees
return 1 + max(left_subtree_length, right_subtree_length)

# Create the nodes and define the structure of the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Calculate the length of the binary tree using the tree_length function and printing the result
print("Length of the binary tree is:", tree_length(root))