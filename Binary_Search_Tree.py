
""" 
Binary Search Tree(BST): 
For each node, the values in left subtree are all smaller than its value, and the values in its right subtree are all larger than its value. 
        10 
    5       14 
 1    7   12   20 

 Inorder Traversal: 1,5,7m10m12m4m20

Properties: 
 1. Each node is also a binary search tree <=> Binary Search Tree
 2. Inorder traversal outputs nodes in increasing order <=> Binary Search Tree 

Usage: 
- Provides ordered data structure
- Use as database's index 

Given BST definition, we could search/delete/insert a node with O(height) time. 
"""

class BstNode():
    def __init__(self,student):
        """
        Introducing Key and Value, key is used for identity, access and compariion. 
        Value is the actual data.
        """
        self.key = student.id 
        self.val = student # the instance of STUDETN class 
        self.left = None
        self.right = None 

# Binary Search Tree Operations 
## Traversal/ Validation 
"""
Validate whether a given binary tree is a binary search tree or not 
"""
def inorder(root, results):
    # base case 
    if root is None: 
        return 
    # recursive rule
    inorder(root.left,results)
    results.append(root.val)
    inorder(root.right,results)
    return 

def valid (root): 
    res = []
    inorder(root, res)
    # result are suppoesd to be in ascending order
    for i in range(len(res) - 1): 
        if res[i] >= res [i+1]:
            return False 
    return True 

# optimazition 
def inorder_v2(root, prev):
    # base case 
    if root is None: 
        return True 
    # recursive rule
    if inorder(root.left,prev) == False: 
        return False 
    if prev[0] >= root.val: 
        return False
    prev[0] = root.val
    if inorder(root.right, prev) == False:
        return False 
    return True

def is_bst_v2(root):
    prev = [float("-inf")]
    return inorder_v2(root,prev)