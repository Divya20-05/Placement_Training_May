# create a 2D matrix and find the sum of the 2D matrix using 2 for loops
# def sum_2d_matrix(matrix):
#     sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             sum += matrix[i][j]
#             return sum
#         return sum
#     return sum
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# rows=len(matrix)
# cols=len(matrix[0])
# sum=0
# for i in range(rows):
#     for j in range(cols):
#         sum+=matrix[i][j]
#         #print(sum)  
# print(sum)

#count the prime numbers in the given 2d list
# m = [[1, 2, 3], [4,6,6], [7, 8, 9]]
# rows = len(m)
# cols = len(m[0])
# count = 0
# for i in range(rows):
#     for j in range(cols):
#         num = m[i][j]
#         if num > 1:
#             is_prime = True
#             for k in range(2, num):
#                 if num % k == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 count += 1
# print(count)

# create a matrix take the input from user and print the matrix using functions
# def get_matrix(m,i,j,p,n):
#     if i==n-1 and j==n-1:
#         print(p)
#         return
#     if (i+1<n and m[i+1][j]==1):
#         get_matrix(m,i+1,j,p+"D",n)
#     if (j+1<n and m[i][j+1]==1):
#         get_matrix(m,i,j+1,p+"R",n)

# m = [[1,1,1,0],
#      [0,1,1,0],
#      [1,0,1,0],
#      [0,0,0,1]]
# get_matrix(m,0,0,"",len(m))

# def fire(m,i,j):
#     if not m:
#         return
#     if i<0 or i>=len(m) or j<0 or j>=len(m) or m[i][j]!=1:
#         return
#     m[i][j]=2
#     fire(m,i+1,j)
#     fire(m,i-1,j)
#     fire(m,i,j+1)
#     fire(m,i,j-1) 
#     return m
# m=([[1,1,1,0,1],
#      [0,1,1,0,1],
#      [1,0,0,1,0],
#      [1,0,0,1,1]])
# count=0
# print(fire(m,0,0))
# for i in range(len(m)):
#     for j in range(len(m[0])):
#         if m[i][j]==1:
#             count+=1
# print(count)  

# def binary(n,res=""):
#     if n==0:
#         print(res)
#         return
#     binary(n-1,res+"0")
#     binary(n-1,res+"1")
# n=2
# binary(n) 

def binary(n,res="",o=0,c=0):
    if o==n and c==n:
        print(res)
        return
    if o<n:
        binary(n,res+"(",o+1,c)
    if c<o:
        binary(n,res+")",o,c+1)
n=3
binary(n)