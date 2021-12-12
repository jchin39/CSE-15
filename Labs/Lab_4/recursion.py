import sys
sys.setrecursionlimit(100000)

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)
    # Provide your code here

print("factorial(5):", factorial(5))
# Expected 120
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    # Provide your code here

print ("fib(7):", fib(7))
# Expected 13

def equal(A, B):
    if len(A) == 0 and len(B) == 0:
        return True
    elif len(A) == 0:
        return False
    elif len(B) == 0:
        return False
    elif A[len(A)-1] != B[len(B)-1]:
        return False
    else:
        A = A[1:len(A)]
        B = B[1:len(B)]
        return equal(A, B) 
print ("equal('ALICE', 'BOB):", equal('ALICE', 'BOB'))
# Expected False
print ("equal('ALICE', 'ALICE'):", equal('ALICE', 'ALICE'))
# Expected True 

def addup(list):
    if len(list) == 1:
        return list[0]
    else:
        x = list[0]
        list = list[1:len(list)]
        return x + addup(list)
    # Provide your code here

print ("addup([1,2,3,4,5]):", addup([1,2,3,4,5]))
# Expected 15
print ("addup(range(101)):", addup(range(101)))
# Expected 5050

def reverse(A):
    if len(A) == 0:
        return A
    else:
        B = A[0]
        A = A[1:len(A)]
        return reverse(A) + B
    # Provide your code here
print ("reverse('hello'):", reverse('hello'))
# Expected olleh