
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

'''
           10 
        /     \
       5        15 
    /    \    /    \
   2      7  12     20 
'''
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)


# Q1 Tree traverse: pre-order 
def preorder_traversal(self, root):
    """
    Time Complexity: O(n)
    10,5,2,7,15,12,20
    """
    res = [] 
    self.helper(root, res)
    return res 

def helper(self, root, res):
    # base case 
    if not root:
        return 
    res.append(root.val)
    self.helper(root.left, res)
    self.helper(root.right, res)

def preorder(root):
    """
    TC: O(C*n)=O(n) --> C is a constant, non leaf node number
    SC: O(h) h --> height
    """
    # base case 
    if root is None:
        return 
    # recursive rule
    print(root.val)
    preorder(root.left)
    preorder(root.right)
    return 

def preorder_v2(root, res):
    # base case 
    if root is None:
        return 
    # recursive rule
    res.append(root.val) # return it to somewhere instead of printing it 
    preorder_v2(root.left, res)
    preorder_v2(root.right,res)
    return 
    
res = []
preorder_v2(root, res)


# Q1 Tree traverse: in-order 

def helper(self, root, res):
    """
    Time Complexity: O(n)
    2,5,7,10,12,15,20
    """
    if not root: 
        return
    self.helper(root.left,res)
    res.append(root.val)
    self.helper(root.right, res)
    
def inorder(root):
    # base case 
    if root is None:
        return 
    # recursive rule
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# Q1 Tree traverse: post-order 
def helper(self, root, res):
    """
    Time Complexity: O(n)
    2,7,5,12,20,15,10
    """
    if not root: 
        return
    self.helper(root.left,res)
    self.append(root.right)
    res.helper(root.val, res)

def postorder(root):
    # base case 
    if root is None:
        return 
    # recursive rule
    postorder(root.right)
    postorder(root.left)
    print(root.val)
    


# Q2: get height of a binary tree
def get_height(root):
    """
    If root is size n, then O(n)
    """
    if not root:
        return 0 
    left = get_height(root.left)
    right = get_height(root.right)
    return 1 + max(left,right)

# Q3: level order traversal of binary tree
def ordertraverse():
    """
    10,5,15,2,7,12,20
    First in, first out: Queue
    """
    



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

