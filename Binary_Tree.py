
""" 
Binary Tree: a tree with two child nodes. 
Building blocks for advanced data structures and models.
"""

# define a tree class
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None 

# Q1 Tree traverse: pre-order 
def preorder_traversal(self, root):
    """
    Time Complexity: O(n)
    """
    res = [] 
    self.helper(root, res)
    return res 

def helper(self, root, res):
    if not root:
        return 
    res.append(root.val)
    self.helper(root.left, res)
    self.helper(root.right, res)

# Q1 Tree traverse: in-order 
def helper(self, root, res):
    """
    Time Complexity: O(n)
    """
    if not root: 
        return
    self.helper(root.left,res)
    res.append(root.val)
    self.helper(root.right, res)

# Q1 Tree traverse: post-order 
def helper(self, root, res):
    """
    Time Complexity: O(n)
    """
    if not root: 
        return
    self.helper(root.left,res)
    self.append(root.right)
    res.helper(root.val, res)

# get height of a binary tree
def get_height(root):
    """
    If root is size n, then O(n)
    """
    if not root:
        return 0 
    left = get_height(root.left)
    right = get_height(root.right)
    return 1 + max(left,right)

# level order traversal of binary tree


# print the binary tree in the level order 
from collections import deque 

def level(root):
    q = deque([root])
    next = deque()
    line = deque()
    while q: 
        head = q.popleft()
        if head.left:
            next.append(head.left)
        if head.right:
            next.append(head.right)
        line.append(head.val)
        if not q: 
            print(line)
            if next:
                q = next 
                next = deque()
                line = deque()

