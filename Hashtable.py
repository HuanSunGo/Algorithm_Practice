
""" 
Dictionary

For any data structure, focus on Create, Add, Delete, Update, Look-up.
Time Complexity: O(1) why?
Space Complexity: O(n)
"""

from operator import le


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

# Q1: Count word occurences in a word array.
def words_to_frequencies(words):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    freqs={}
    for word in words:
        if word in freqs:  # O(1): using keys to search 
            freqs[word] += 1 
        else:
            freqs[word] = 1
        print(freqs) # for debug 
    return freqs 

words = ['abc', 'abc','cba','cba']
output = words_to_frequencies(words)

# Q2: Most common word in a frequency dictionary
def most_common_words(freqs):
    best = max(freqs.values())  # O(n)
    words=[] 
    for word, count in freqs.items():
        if count == best:
            words.append(word)
    return (word,best)

most_common_words(output) # max only return one, but here losing the (abc,2) case? 

## tuple unpack:
word, count = ('abc',2) , ('cba', 2)

""" 
Set

Def: Unordered collection of unique elements. Special case of dict with only keys. 
Traits: Do not record element position or order of insertion, 
        do not support indexing, slicing, or other sequence-like behavior.

"""

X = {'a','b','c','d'}

X.add('e')
X.update({'e','f'}) # add multiple elements 
X.remove('a') # delete an element, if element doesn't exist, raise a KeyError
X.discard('f') # no KeyError raised 
X.pop() # delete one random element 
X.clear() # clear elements from the set 

a={'postcard','radio','telegram'}
b={'radio','television'}

print(a.difference(b))
print(b.difference(a))
print(a.intersection(b))

# Q2: Palindromic Testing 
def is_palindromic(word):
    """
    Given a string, check if it's can be written palindromically.
    e.g. 'edified' can be permuted to form 'deified'.

    Hash: letter -> count 

    Rules: at most having one character that with odd occurence.

    Time Complexity: O(n)
    Space Complexity: O(n), or O(c) --> c: distinct letters in the string, and with maximum of 26 
    """
    freq= {}
    for letter in word:
        if letter in freq:
            freq[letter] += 1 
        else:
            freq[letter] = 1
    odd_count = 0
    for value in freq.values():
        if value % 2 == 1:
            odd_count += 1 
            if odd_count > 1:
                return False
    return True 




