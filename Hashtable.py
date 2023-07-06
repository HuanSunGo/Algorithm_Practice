
""" 
Dictionary

For any data structure, focus on Create, Add, Delete, Update, Look-up.
Time Complexity: O(1) 
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
        Better for just check the existence. 

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
    e.g. 'deified' can be permuted to form 'deified'.

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

# Q3. Sliding window with hashtable
from collections import defaultdict 
def find_longest_substr(s,k):
    """
    You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

    For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
    """
    left = ans = 0
    counts = defaultdict(int)
    for right in range (len(s)):
        counts[s[right]] += 1 
        while len(counts) > k:
            # here we don't want to get the over the number of k
            counts[s[left]] -= 1 
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1 
        ans = max(ans, right-left+1)

    return ans 

# LC 2238. Interesction of Multiple Arrays 
from collections import defaultdict 
class Solution: 
    def intersection(self, nums:List[List[int]]) -> List[int]:
        """
        For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

        The occurence of the number should be the numberr of the lists that's within the outer list, use hashmap to count and iterate.
        """
        len_nums = len(nums)
        counts = defaultdict(int)
        ans = []
        for i in len_nums:
            for j in len(nums[i]):
                counts[j] += 1 
        
        for key in counts.keys:
            if counts[key] == len_nums:
                ans.append(counts.values)
        
        return ans 

# LC 560. Subarray Sum Equals K 
def subarraySum(nums,k):
    """
    Map the prefix to the frequencies.
    """
    counts = defaultdict(int)
    # empty subarry [] is a subarray with sum 0
    count[0] = 1
    ans = curr = 0
    
    for num in nums:
        # add eacg bynver to the prefix sum
        curr += num
        # check if the current prefix sum minus k has appeared already
        ans += counts[curr - k]
        counts[curr] += 1 


    pass 