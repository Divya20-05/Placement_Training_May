# n=int(input())
# if (n&(n-1))==0:
#     print("True")
# else:
#     print("False")
# #print((n&(n-1))==0 and n!=0)

#sum of odd indices in an given array with out functions

# arr=list(map(int,input().split()))
# sum=0
# for i in range(len(arr)):
#     if i%2!=0 and arr[i]%2==0:
#         sum+=arr[i]
# print(sum)

#
# l=list(map(int,input().split()))
# max=0
# count=0
# for i in l:
#     if i>max:
#         max=i
#         count=1
# print(count)

#
# n=int(input())
# crimes =list(map(int,input().split()))
# officer=0
# untreated=0
# for i in crimes:
#     if i ==-1:
#         if officer>0:
#             officer-=1
#         else:
#             untreated+=1
#     else:
#         officer += i
# print(untreated)

# n=int(input())
# vote=list(map(int, input().split()))
# age=list(map(int,input().split()))

# candidate=max(vote)*[0]

# for i in range(n):
#     if (age[i]>=18):
#         candidate[vote[i]-1]+=1
#     else:
#         candidate[vote[i]-1]+=0
# print(max(candidate)) 

# a=7 #(101)
# b=5 #(111)
# a=a^b
# b=a^b
# a=a^b
# print(a)
# print(b)  

# l=[1,2,3,4,5,6,7]
# l.append([1,2,3])
# l.extend([1,2])
# l.extend(2)
# l.extend({1,2,3,4,5,6})
# print(len(l))

n=int(input())
if n%4==1:
    print(1)
if n%4==2:
    print(n+1)
if n%4==3:
    print(0)
if n%4==0:
    print(n)
# x=0
# for i in range(1,n+1):
#     x^=i
# print(x)

