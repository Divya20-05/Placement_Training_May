# # Sortings

# # Bubble sort without functions
# arr=[64, 34, 25, 12, 22, 11, 90]
# n=len(arr)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

# # arr=[64, 34, 25, 12, 22, 11, 90]
# # n=len(arr)
# # for i in range(n):
# #     flag=False
# #     for j in range(0, n-i-1):
# #         if arr[j]>arr[j+1]:
# #             arr[j],arr[j+1]=arr[j+1],arr[j]
# #             flag=True
# #     if not flag:
# #         break
# # print(arr)

# # selection sort without functions
# arr=[12,11,13,5,6]
# n=len(arr)
# for i in range(n):
#     min=i
#     for j in range(i+1,n):
#         if arr[j]<arr[min]:
#             min=j
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)

# #Insertion sort without functions
# arr=[10,5,3,2,6]
# n=len(arr)
# for i in range(n):
#     k=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>k:
#         arr[j+1]=arr[j]
#         j-=1
#     arr[j+1]=k
# print(arr)


# # Input: [3,6,1,7,4,2,5]
# # output:[6,4,2,1,3,5,7]
# #give the code
# arr=[3,6,1,7,4,2,5]
# even=[]
# odd=[]
# for i in arr:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# even.sort(reverse=True)
# odd.sort()
# arr=even+odd
# print(arr)


# arr=[3,6, 1, 7, 4, 2, 5]
# result = []
# for i in sorted(arr,reverse=True):
#     if i%2== 0:
#         result.append(i)
# for j in sorted(arr):
#     if j%2!=0:
#         result.append(j)
# print(result)
  
# # Write the code for the largest element in the array
# arr=[3,6,1,7,4,2,5]
# max=0
# for i in arr:
#     if i>max:
#         max=i
# max1=0
# for i in arr:
#     if i>max1 and i!=max:
#         max1=i
# print(max)
# print(max1)

# a=[3,2,6,4,7,1,5]
# k=4
# n=len(a)
# for i in range(k):
#     for j in range(0,n-1-i):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
# print(a[-k])

# # [2,3,5,1,6,9,8]
# # k=2
# # [2,3,1,5,6,9,8]
# arr=[2,3,5,1,6,9,8]
# k=2
# n=len(arr)
# for i in range(k):
#     for j in range(0,n-1-i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

# # [[1,2],[5,1],[2,4],[6,3]]
# # [[5,1],[1,2],[6,3],[2,4]]
# arr=[[1,2],[5,1],[2,4],[6,3]]
# n=len(arr)
# for i in range(n):
#     for j in range(0,n-1-i):
#         if arr[j][1]>arr[j+1][1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

# # [[20,12,11],[10,5,22],[16,7,30]]
# # sort according to the prime number
# # arr=[[20,12,11],[10,5,22],[16,7,30]]
# # n = len(arr)
# # def is_prime(n):
# #     if n<2:
# #         return False
# #     for i in range(2,int(n**0.5)+1):
# #         if n%i==0:
# #             return False
# #     return True
# # def get_prime(inner_list):
# #     for num in inner_list:
# #         if is_prime(num):
# #             return num
# #     return float('inf')  
# # for i in range(n):
# #     for j in range(0, n - i - 1):
# #         if get_prime(arr[j])>get_prime(arr[j + 1]):
# #             arr[j],arr[j + 1] =arr[j+1],arr[j]
# # print(arr)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# l=[[20,12,11],[10,5,22],[16,7,30]]
# p = []

# for row in l:
#     for num in row:
#         if is_prime(num):
#             p.append(num)

# for i in range (0,len(l)):
#   for j in range (0,len(l)-i-1):
#     if p[j]>p[j+1]:
#       p[j],p[j+1]=p[j+1],p[j]
#       l[j],l[j+1]=l[j+1],l[j]
# print(l)

# [a,b,b,b,c,c]
# [a,c,c,b,b,b]
# arr=[a,b,b,b,c,c]
# arr=sorted(arr)
# print(arr) 
# from collections import Counter
# arr = ['a', 'b', 'b', 'b', 'c', 'c']
# freq = Counter(arr)
# result = []
# chars_sorted = sorted(freq, key=lambda x: freq[x])
# for ch in chars_sorted:
#     result.extend([ch] * freq[ch])
# print(result)

m=[[1,0,0,1],
   [1,1,0,0],
   [0,1,0,1]]
a=[4,3,5,7]
for i in range(len(m)):
    sum=0
    for j in range(len(m[0])):
        if m[i][j]==1:
            sum+=a[j]
    print(sum)