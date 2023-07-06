"""
LinkedList is a data structure for storing a collection of items, that is either empty(null) or a reference to a node object.
A string of nodes(boxes) linked by pointers, within each node contains `data` and `next` attribute.
The first and last node are called the head and tail.

Why need a linked list?
1. Versatility and flexibility, does not require to know the size ahead. 
2. Being able to model the link based relationship directly.Fundamental to tree. 
"""
## Q1: Traverse

# Node class

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None	
"""
	def __str__(self):
		
		__str__() # directly call the class and print, will only print out the location
		__eq__() # equa, x==y
		__ge__() # greater than, x >= y
		__le__() # less than, x <= y 
		
		# in order to print the value instead of the position
		return str(self.val) 
"""

arr = ["H", "E", "A", "P"]

# Build a LinkedList, that contains the node object
def create_list(arr): 
	head = ListNode(arr[0])
	curr = head 
	for i in range(1, len(arr)): 
		curr.next=ListNode(arr[i])
		curr=curr.next
	return head # as long as able to find the head, the following are able to get


def buildList(seq):
    # seq is a list of objects. f is the fake head 
    f = ListNode(None)
    c = f
    for obj in seq:
        c.next = ListNode(obj)
        c = c.next
    h, f.next = f.next, None # interrupt the connection of fake head. or without this sentence, and directly return f.next
    return h


def print_all_nodes(head):
    """
    Print all the nodes inside a singly linked list and print.  
	Assume head refers to the head node of a singly linked list.
    """
    while head is not None:
        print(head.val)
        head = head.next 
        
h = buildList([1,2,3,4])
print_all_nodes(h)

## Q2: Search by index. Given a singly linked list and an index, return the node you found, otherwise None.

def search_by_index(head, index):
	# here we want to find the node itself, other than the previous that need to fix the head
	if index < 0 or head is None: 
		return None 
	curr_idx = 0 # only serving as a pointer, have no val-next attribute 
	while head is not None: # the quit case is traverse till the end 
		if curr_idx == index : 
			return head # what we want is the node, not the index itself 
		else: 
			curr_idx += 1 
			head = head.next # move the pointer 
	return None 

def search_by_value(head, value):
	if head is None:
		return None
	curr_idx = 0
	while head is not None:
		if head.val == value:
			return head
		else:
			curr_idx += 1 # serve as a int pointer, have no val attribute, and kinda redundant
			head = head.next 
	return None

def search_by_value_example(head, value):
	if not head:
		return None
	current_node = head 
	while current_node is not None:
		if current_node.val == value:
			return current_node 
		current_node = current_node.next
	return None 

# compare 
n1, n2= ListNode(1), ListNode(1)
print(n1==n2) # will return False because are different object 

search_by_index(h,3)

## Q3: Add to the index. 
"""
Given a singly linked list, an index(assuming the first list node is 0) and target value, 
add a new node before the node at the specified position.
Return the head of the singly linked list after insertion. 

n1 -> n2 -> none, index = 1, value = 4 
	  index
n1 -> 4 -> n2 -> none
index-1 

"""
def add_to_index(head, index, value):
    # the case when inserting to the first position (head)
    if index == 0:
        new_head = ListNode(value)
        new_head.next = head
        return new_head 
    else: 
        # preNode points to the node that precedes the node at the insertion position
        preNode = search_by_index(head, index-1)

		# the case when inserting to the last position (tail)
        if preNode is None:
            return head 

        new_node = ListNode(value)
		# insert n2 after n first
        new_node.next = preNode.next
        preNode.next = new_node 
        return head 

def add_to_index_fake(head, index, value):
	"""
	Adding sentinel to remove additional logic branches. 
	Since the head of a singly linked list is a special node that has no predecessor, to avoid the special case handling,
	can manually add a dummy node before and use it as the new head. 
	
	1 -> None, index = 0, value = 4
	fake -> 4 -> 1 ->None
	4 -> 1 -> None 
	"""
	fake = ListNode(None) # the val isn't important 
	fake.next = head 
	prev = search_by_index(fake, index) # not index-1 anymore 
	if prev is None: 
		return head # fake.next 
	new_node = ListNode(value)
	new_node.next=prev.next
	prev.next = new_node 
	return fake.next 

## Q4: Remove from the index. 
"""
Other than the info about the current node and the predecessor,
the sucessor info is also needed, which is None. 
"""
def remove_from_index(head, index):
	fake = ListNode(None)
	fake.next = head 
	prev= search_by_index(fake, index)
	# the case when we're at the last
	if prev is None or prev.next is None:
		return fake.next 
	rm_node = prev.next
	prev.next = rm_node.next 
	rm_node.next = None
	return fake.next


## Q5: Design a linked list class. 
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None	

class my_linkedlist: 
	def __init__(self):
		"""
		Initialize the data structure here, construct an empty linked list.
		"""
		self.head = None
		self.tail = None
		self.size = 0
	
	def get_node(self, index):
		"""
		Helper function for pointing to the specific node. 
		"""
		curr = self.head 
		for i in range(index):
			curr = curr.next 
		return curr 

	def get(self, index): 
		"""
		Get the value of the index-th node in the linked list.
		If the index is invalid, return -1.
		"""
		if index < 0 or index >= self.size:
			return -1
		node = self.get_node(index) # write the helper function 
		return node.val 
		

	def add_at_head(self, val):
		"""
		After the insertion, the new node will be the head.
		"""
		if self.size == 0: 
			self.head = ListNode(val)
			self.tail = self.head # cannot go with ListNode(val), for these are stored at different locations, are seperate two nodes
		# no need to change the tail other than the corner case 
		else : 
			new_head = ListNode(val)
			new_head.next = self.head
			self.head = new_head 
		self.size += 1 


	def add_at_tail(self, val):
		"""
		Append a node of value to the last element of the linked list. [Need revise]
		"""
		if self.size == 0: 
			self.head = ListNode(val)
			self.tail = self.head 
		else : 
			new_tail = ListNode(val)
			self.tail.next = new_tail
			new_tail.next = None
		self.size += 1 

	def add_at_index(self, index, val):
		"""
		If index equals to the length of list, the node will append at the end of the list, 
		if greater than the length, then cannot be inserted. 
		"""
		if self.size < 0 or index > self.size: 
			return None
		if index == 0:
			self.add_at_head(val)
		elif index == self.size:
			self.add_at_tail(val)
		else: 
			prev = self.get_node(index-1)
			new_node=ListNode(val)
			new_node.next = prev.next
			prev.next = new_node
			self.size += 1 
			
	def delete_at_index(self, index, val):
		"""
        Delete the index-th node in the linked list, if the index is valid.
			:type index: int
			:rtype: None
        """
		fake = ListNode(val)
		fake.next = self.head 
		prev = self.get_node(fake,index)
		if prev is None or prev.next is None:
			return fake.next 
		rm_node = prev.next
		prev.next = rm_node.next 
		rm_node.next = None 
		
		return fake.next 

my_list=my_linkedlist()
my_list.add_at_head(1)
my_list.add_at_tail(9)

## Q6: Double Linked List
class ListNode:
	def __init__(self, value):
		"""
		n1 <-> n2, insert n between n1 and n2: 
		n.next=n2
		n.prev=n1
		n1.next=n
		n2.prev=n
		"""
		self.value = value 
		self.next = None
		self.prev = None 

## Q7: Remove all vowels in a linked list.
class ListNode:
	def __init__(self, value):
		self.val = value 
		self.next = None 

def remove_vowels(head):
	"""
	Time Complexity: O(n)
	Space Complexity: O(5*2) --> O(C) --> O(1) ? 
	"""
	fake_head = ListNode(None)
	fake_head.next = head 
	prev = fake_head
	curr = head 
	vowel = ['a','e','i','o','u'] # O(5)
	vowel = set(vowel) # O(1) set is faster 
	while curr :  # while curr is not None 
		if curr.val in vowel:
			prev.next = curr.next 
		else:
			prev = prev.next 
		curr = curr.next 
	return fake_head.next 

def print_list(node):
	a = []
	while node is not None:
		a.append(node.val)
		node = node.next 
	print(a)

# test code 
node_b = ListNode('b')
node_i = ListNode('i')
node_e = ListNode('e')
node_b.next = node_i 
node_i.next = node_e 

print_list (node_b)
new_head = remove_vowels(node_b)
print_list(new_head)

## Q8: Determine if a LinkedList is panlidrome. 
def find_mid(head):
	"""
	Logic
	----------------
	Fast and slow pointer: 1) find mid, 2) reverse 2nd half, 3) compare 
	"""
	if head is None or head.next is None:
		return head 

	slow = head 
	fast = head 
	while fast and fast.next and fast.next.next: 
		fast = fast.next.next 
		slow = slow.next 
	return slow 

def reverse_list(head):
	prev = None 
	while head:
		next_node = head.next 
		head.next = prev
		prev = head 
		head = next_node 
	return prev

def is_palindrome(head):
	if head is None: 
		return True
	mid_node_prev = find_mid(head)
	# A  B  C   E  F  G
	#       MP  M
	second_half = mid_node_prev.next 
	mid_node_prev.next = None # cut off C and E 
	head1 = head 
	head2 = reverse_list(second_half)
	while head1 and head2:
		if head1.val != head2.val:
			return False
		head1 = head1.next
		head2 = head2.next 
	return True 

# test code 
node1 = ListNode(1)
node2= ListNode(2)
node0 = ListNode(0)
node1.next = node2
node2.next = node0
print(is_palindrome(node1))

	
## LeetCode 21: Merge Two Sorted Lists 

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        # base case 
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        # recursive ruel
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2) 
            return l1
        else: # l1.val > l2.val 
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class ListNode:
	def __init__(self, value, next=None):
		self.val = value 
		self.next = next 

def merge(one, two):
    """
    input: ListNode one, ListNode two
    return: ListNode
    """
    # write your solution here
    three = ListNode(0)
    head = three
   
    while one and two:
      if one.val < two.val:
        three.val = one.val
        one = one.next
      else:
        three.val = two.val
        two = two.next 
      
    if one:
        three.next = one
    else:
        three.next = two

    return head

a, b = ListNode(1), ListNode(1, ListNode(2)) # 1, 1->2
print_list(merge(a,b))