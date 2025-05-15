#print the output : 1 2 3 4 5 4 3 2 1
# def func(n):
#     for i in range(1,n+1):
#         print(i,end=" ")
#     for i in range(n-1,0,-1):
#         print(i,end=" ")
#     print("\n")
# n=5
# func(n)
# n=int(input())
# for i in range(1,n+1):
#     print(i,end=" ")
# for i in range(n-1,0,-1):
#     print(i,end=" ")

#5 4 3 2 1
# def func(n):
#     if n==0:
#         return 200
#     print(n,end=" ")
#     func(n-1)
#     #print(n,end=" ")
# n=5
# print(func(n))

# def func(n):
#     if n==0:
#         return 
#     print(n,end=" ")
#     func(n-1)
#     if n!=1:
#         print(n,end=" ")
# n=5
# func(n)
# print("\n")

#odd even
# def func(n):
#     if n==0:
#         return 
#     if n%2!=0:
#         print(n,end=" ")
#     func(n-1)
#     if n!=1:
#         if n%2==0:
#             print(n,end=" ")
# n=5
# func(n)

#1 2 3 4 5 4 3 2 1
# def func(n,m=1):
#     if m>n:
#         return
#     print(m,end=" ")
#     func(n,m+1)
#     if m!=n:
#         print(m,end=" ")
# n=5
# func(n)
#
# def func(n,m=0):
#     if m==n:
#         return
#     print(m+1,end=" ")
#     func(n,m+1)
#     if (m+1)!=n:
#         print(m+1,end=" ")
# n=5
# func(n) 

#1. all natural numbers till 'n' using recursion
# def natural(n):
#     if n==0:
#         return
#     natural(n-1)
#     print(n,end=" ")
# n=10
# natural(n)

# 2. display odd from 1 to 100 using recursion
def odd(n):
    if n>100:
        return
    print(n,end=" ")
    odd(n+2)
odd(1)

# 3. even numbers from 1 to 100 using recursion
def even(n):
    if n%2==0:
        print(n,end=" ")
    if n>100:
        return
    even(n+1)
even(1)

# 4. factorial of a number using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

# 5. given number prime or not using recursion
def prime(n,i):                         # n=int(input())
    if i==n: # 5                        # flag=0
        return True                     # for i in range(2,n//2):       # for i in range(2,int(n**(1/2))+1):
    if n%i==0:                          #     if n%i==0:
        return False                    #           flag+=1
    return prime(n,i+1)                 #           break
n=17                                    # if flag==0:
print(prime(n,2))                       #      print("prime")
#  def is_prime(n,i=2):                 # else:
        # if i*i>n:                     #      print("not prime")
        #     return True
        # if n%i==0:
        #     return False  
        # return is_prime(n,i+1)            
                            
# 6. fibonacci series using recursion
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i),end=" ")
print()

# 7. reverser the given number using recursion
def reverse(n,rev=0):
    if n==0:
        return rev
    return reverse(n//10,rev*10+n%10)
n=3456789
print(reverse(n))

# 8.palindrome of a given number using recursion
def palindrome(n,rev=0):
    if n==0:
        return rev
    return palindrome(n//10,rev*10+n%10)
n=12321
print(palindrome(n))

# write a code to print minimum steps to reach
# def fun(n):
#   if n==1:
#     return 0
#   elif n%2==0:
#     return 1+fun(n//2)
#   else:
#     return 1+min(fun(n-1)),fun(n+1)

# n=int(input())
# print(fun(n))

# sum of all the elements of a list using recursion
def fun(l,i=0):
    if i==len(l):
        return 0
    return l[i]+fun(l,i+1)
l=[1,4,3,2,5]
print(fun(l))

# count of all prime number in the list using recursion
def prime(n,i=2):
    if i*i>n:
        return True
    if n%i==0:
        return False
    return prime(n,i+1)

def fun(l,i=0):
    if i==len(l):
        return 0
    if prime(l[i]):
        return 1+fun(l,i+1)
    return fun(l,i+1)
l=[11,4,3,6,5,17]
print(fun(l))