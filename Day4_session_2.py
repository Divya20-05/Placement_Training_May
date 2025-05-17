# 1+2+3+4+5
# parameterized recursion
# def fun(n,sum):
#     if n<1:
#         print(sum)
#         return 
#     fun(n-1,sum+n)
# n=5
# fun(n,0)

# def fun(n):
#     if n==0:
#         return 0
#     return n+fun(n-1)
# n=5
# print(fun(n)) 

# write a code to find a subset of given list
def subset(n,index=0,res=[]):
    if index==len(n):
        print(res)
        return []
    subset(n,index+1,res+[n[index]])
    subset(n,index+1,res)
l=[1,2,3]
subset(l)

# write a program to find the subset sum of a given number
def subset_sum(n,k,index=0,res=[]):
    if index==len(n):
        if sum(res)==k:
            print(res)
            return
        return
    subset_sum(n,k,index+1,res+[n[index]])
    subset_sum(n,k,index+1,res)
n=[1,2,3,6]
k=10
subset_sum(n,k)

def fun(arr,i,k):
    if k==0:
        return True
    if i==0:
        return False
    if arr[i-1]>k:
        return fun(arr,i-1,k)
    return fun(arr,i-1,k) or fun(arr,i-1,k-arr[i-1])
arr=[1,2,3,8]
k=5
print(fun(arr,len(arr),k))

# [1 3 5 1 2 2 3 3 5 2 1]
# print the frequency between the given target number from a given list using recursion
# def freq(arr,i,target):
#     if i==len(arr):
#         return 0
#     if arr[i]==target:
#         return 1+freq(arr,i+1,target)
#     return freq(arr,i+1,target)
# arr=[1,3,5,1,2,2,3,3,5,2,1]
# target=5
# print(freq(arr,0,target))

# Dislike Threes
t = int(input())
queries = [int(input()) for _ in range(t)]
valid = []
i = 1
while len(valid) < 2000:
    if i % 3 != 0 and i % 10 != 3:
        valid.append(i)
    i += 1
for k in queries:
    print(valid[k - 1])

# t=int(input())
# for _ in range(t):
#     i=1
#     count=0
#     k=int(input())
#     while(1):
#         if i%3!=0 and i%10!=3:
#             count+=1
#             if count==k:
#                 print(i)
#                 break
#         i+=1


