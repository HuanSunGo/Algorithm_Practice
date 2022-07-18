"""
LinkedList is a data structure for storing a collection of items, that is either empty(null) or a reference to a node object.
A string of nodes(boxes) linked by pointers, within each node contains `data` and `next` attribute.
The first and last node are called the head and tail.

Why need a linked list?
1. Versatility and flexibility, does not require to know the size ahead. 
2. Being able to model the link based relationship directly.Fundamental to tree. 
"""

# Node class
class node:
	def __init__(self,data):
		self.data=data # sometimes also refers to as `value` 
		self.next=None

# Linked List class contains a Node object
class linked_list:

	# Function to initialize head
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	# Prints out the linked list in traditional Python list format. 
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print (elems)

	# Returns the value of the node at 'index'. 
	def get(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print ("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video
			print ("ERROR: 'Erase' Index out of range!")
			return 
		cur_idx=0
		cur_node=self.head
		while True:
			last_node=cur_node
			cur_node=cur_node.next
			if cur_idx==index:
				last_node.next=cur_node.next
				return
			cur_idx+=1
            

my_list=linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()


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
    # seq is a list of objects.
    f = ListNode(None)
    c = f
    for obj in seq:
        c.next = ListNode(obj)
        c = c.next
    h, f.next = f.next, None # why doing this? 
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
	curr_idx = 0 
	while head is not None: # the quit case is traverse till the end 
		if curr_idx == index : 
			return head # what we want is the node, not the index itself 
		else: 
			curr_idx += 1 
			head = head.next # move the pointer 
	return None 

# compare 
n1, n2= ListNode(1), ListNode(1)
print(n1==n2) # will return False because are different object 

search_by_index(h,3)

## Q3: Add to the index. 
"""
Given a singly linked list, an index and target value, 
add a new node before the node at the specified position.

n1 -> n2, insert n 
	  index
n1 -> n -> n2 
index-1 

"""
def add_to_index(head, index, value):
    # head: type is node 
    if index == 0:
        new_head = ListNode(value)
        new_head.next = head
        return new_head 
    else: 
        # preNode points to the node that precedes the node at the insertion position
        preNode = search_by_index(head, index-1)
        if preNode is None:
            return head 
        new_node = ListNode(value)
		# insert n2 after n first
        new_node.next = preNode.next
        preNode.next = new_node 
        return head 

def add_to_index1(head, index, value):
	if index == 0: 
		new_head = ListNode(value)
		new_head.next = head 
		return new_head 
	else:
		preNode = search_by_index(head, index-1)
		if preNode is None: # already exceed the length 
			return head 
		new_node = ListNode(value)
		new_node.head=preNode.mext
		preNode.next = new_node 
		return head 

def add_to_index_fake(head, index, value):
	"""
	1-> None, index=0, value=4
	dummy, fake, sentinel: mannuly add a pointer 

	fake -> 1 -> None 
	fake -> 4 -> 1 -> None 
	4 -> 1 -> None 
	"""
	fake = ListNode(None) # the val isn't important 
	fake.next = head 
	prev = search_by_index(fake, index) # not index-1 anymore 
	if prev is None: 
		return head # fake.next 
	new_node = ListNode(value)
	new_node.head=prev.mext
	prev.next = new_node 
	return fake.next 

		