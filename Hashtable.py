
""" 
For any data structure, focus on Create, Add, Delete, Update, Look-up.
Time Complexity: O(1) why?
Space Complexity: O(n)
"""

grades= {'Ana':'B', 'John':'A','Denise':'A','Katy':'A'}
grades['Sylvan'] # raise KeyError
grades.get('Sylvan','None') 

# Look-up: check if key in dic
'John' in grades 

# Delect entry
del grades['Ana']
grades.pop('Ana')

# get all keys or vales as a list: return in random orders
list(grades.keys())
list(grades.values())
grades.items()

# keys: must be unique, immutable
X= {[1]:10} # TypeError: unhashable type: 'list'
Y= {(1,2):10}