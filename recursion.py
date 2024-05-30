# Recursion is a function that calls itself
# What is QA? Quality Assurance 
# What is a base case? The simplest case of a recursive function

# Test 2 How to solve factorial
def factorial(n):
    if(n <= 1):
        return 1 
    else:
        return n * factorial(n-1)
    

def fibonacci(n):
    if(n <=1 ):
        return n # why return n?  because the first two numbers in the fibonacci sequence are 0 and 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # why n-1 and n-2?  because the fibonacci sequence is the sum of the two previous numbers