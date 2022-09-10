"""
ASCII: American Standard Code for Information Interchange eg. A == 65, a == 97
Unicode: An expansion of ASCII. UTF-8: 1 byte - 4 bytes, UTF-16: 2-4 bytes  
----------------------------------------------------------------------------

Method: similary to the arry, use 2 indexs, slow and fast pointer to deal with it.

"""

# Q1.1 char removal: remove a/some particular chars from a string 'student'
def remove_wrong (string):
    for i in range(len(string)):
        # wrong1: IndexError -- when the first u is deleted, the next for loop will excede the scope 
        if string[i] == 'u' or string[i] == 'n':
            # wrong2: if the string is 'stuudent', the 2nd u won't be visited
            string = string[:i] + string[(i+1):]
    return string 

def remove(str):
    """
    i = 0; (slow) all letters to the left of i are all processed letters that should be kept;
    j = 0; (fast) the letter being processed, which means that all letters to the left are processed
    all letters in [i,j-1] are the strings that we'd alread seen but do not care 
    ------------
    TC: 4 * O(n) --> O(n)
    SC: 2: O(n) --> O(n)
    """
    lst = list(str)
    i,j = 0,0
    while j < len(lst):
        if lst[j] not in ['u','n']:
            # if want to keep it, cover the i with the j 
            lst[i] = lst[j]
            i += 1
        j += 1 
    return ''.join(lst[:i])

def remove_v2(str):
    """
    TC:O(2n) --> O(n)
    SC:O(n)
    """
    result = []
    for ch in str: 
        if ch not in ['u','n']:
            result.append(ch)
    return ''.join(result)

# Q1.2: Remove all the leading/trailing and duplicate empty spaces from the input string
def remove_space(str):
    """
    Input: '___abc__de__'
    Output: 'abc_de'
    ---------------------
    case1: lst[j] != ' ', keep
    case2: lst[j] == ' ',
        case2.1: i == 0 or lst[i-1] == ' ', ignore 
        case2.2: otherwise, keep 
    
    Termination: j = n 
    Post-processing: i > 0 and lst[i-1] == ' ', then i -= 1
    """
    if not str:
        return str
    lst = list(str)
    i,j = 0,0
    while j < len(lst):
        if lst[j] != ' ' or (i != 0 and lst[i-1] != ' '):
            lst[i] = lst[j]
            i += 1
        j += 1 
    # remove trailing empty space 
    if i > 0 and lst[i-1] == ' ':
        i -= 1 
    return ''.join(lst[:i])

# Q2: Char de-deplicate: remove duplicated and adjacent letters in a string. 'aabbazw' -> 'abazw'
def remove_deplicate(str) :
    """
    Initialize: j = 1, i = 1. since we always keep the first one
    Case1: lst[j] == lst[i-1], ignore(j+=1)
    case2: lst[j] != lst[i-1], keep(lst[i] = lst[j], i += 1, j += 1)
    """
    if not str or len(str) < 2:
        return str
    lst = list(str)
    i, j = 1,1
    while j < len(lst):
        if lst[j] != lst[i-1]:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i])

# Q2.1: Char de-duplication adjacent letters repeatedly. abbbbaz -> aaz -> z, anana -> ababa
def remove_duplicate_v2(str):
    """
    Look back: stack 
    case1: str[j] != stack.top, then stack.push(str[j])
    case2: str[j] == stack.top, 
            keep moving j until str[j] != stack.top
            stack.pop()
    ---------------------
    TC: O(n) --> the two while loops just keep the process going and not iterating
    """
    if not str or len(str) < 2:
        return str
    stack = []
    j = 0
    while j < len(str):
        if len(stack) > 0 and str[j] == stack[-1]: 
            # skip all the characters that are same with the top
            while j < len(str) and stack[-1] == str[j]:
                j += 1
            stack.pop()
        else:
            stack.append(str[j])
            j += 1
    return ''.join(stack)

# Q3: Reverse.'I love Yahoo' --> 'Yahoo love I' 
def reverse_v1(str):
    """
    split -> reverse [::-1] -> join
    """
    lst = str.split()
    reverse = lst[::-1]
    str_new = ' '.join(reverse)
    return str_new 

# Q4: Substring: check if one string is the substring of another string
def substring_bruteforce(text, pattern):
    """
    Brute force method: try every possible position

    Input: text 'abcde', pattern 'cde'
    Return: -1 False

    ---------------
    TC : O(m*n) --> Optimization: Robin-Karp
    """
    m = len(text)
    n = len(pattern)
    if m < n:
        return -1
    for i in range(0,m-n+1):
        if find_match(text, pattern, i, n):
            return i
    return -1 

def find_match(large, small, start, n):
    for i in range(n):
        if large[start + i] != small[i]:
            return False
    return True