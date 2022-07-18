## Q1: Fibonacci Sequence --> Iteration Method
"""
[0,1,1,2,3,5,8,13,21,...] 

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import Type


def fib_iteration(n):
    a = 0 
    b = 1
    if n == 1: 
        print(a)
    else:
        for i in range(2,n):
            c = a + b 
            a = b 
            b = c 
            print(c) # for debug
    return c 
print(fib_iteration(6))

## Q2: Fibonacci Sequence --> Recursion Method
"""
Recursion: Looks like the functions call itself, yet essentially is boilling down a big problem to smaller ones.

Time Complexity: O(2^n)
Space Complexity: O(n) - call stack cost

Really bad performance unless use the following cache library function.
# from functools import lru_cache
# @lru_cache(maxsize = 1000) 
"""


def fib_recursion(n):
    # base case: the smallest problem to solve 
    if n <= 1:
        return n 
    # recursive rule: how to make the problem smaller 
    return fib_recursion(n-1) + fib_recursion(n-2)

for n in range(1,30):
    print(f"{n}'th fibonacci number: {fib_recursion(n)}")


## Q3: Optimized Fibonacci --> Using Memory

fibonacci_cache={}

def fib_memory(n):
    # first check the type of input
    if type(n) != int:
        raise TypeError("n must be a positve int")
    if n < 1: 
        raise ValueError("n must be a positve int")

    # if we have cached the value, then return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    #compute the Nth term
    if n == 1: 
        value = 1
    elif n == 2:
        value = 1
    elif n > 2: 
        value = fib_memory(n-1) + fib_memory(n-2)

    # cache the value and return it 
    fibonacci_cache[n] = value 
    return value 

for n in range(1,101):
    print(f"{n}'th fibonacci number: {fib_memory(n)}")

## Q4: Calculate the sum from 1 to n
def get_sum(n):
    acc = 0 
    for i in range(1,n+1):
        acc += i 
    return acc 

def compute_sum(n):
    # base case
    if n == 1:
        return 1
    # recursive rule
    return compute_sum(n-1) + n 

## Q5: Print a singly linked list recursively.

## Q6: Reverse a singly linked list. 