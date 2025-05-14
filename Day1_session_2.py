#count the number of prime numbers from range 0 to 30
# n=int(input())
# for i in range(0,n+1):
#     count=0
#     for j in range(1,i):
#         if (n%2==0):
#             count+=1
#     print(count)


#watermelon
# w=int(input("Enter the weight of the watermellon : "))
# if (w%2!=0 or w==2):
#     print("No")
# else:
#     x=w//2
#     print("Yes")
    
# Elephant
# n=int(input())
# if n%5==0:
#     print(n//5)
# else:
#     print(n//5+1)

#
# n,m=map(int,input().split()) #split("#")
# if n%m==0:
#     print(n//m)
# else:
#     print((n//m)+(n%m))   

# a,b=map(int,input().split())
# year=0
# while a<=b:
#     a=a*3
#     b=b*2
#     year+=1
# print(year)

#n=total no of rides Ann needs
#m=no of rides that multi ride covers 
#a=price of nrml ticket
#b=price of multi ride ticket
n,m,a,b=map(int,input().split())
c1=n*a
c2=((n+m-1)//m)*b
c3=(n//m)*b+(n%m)*a
print(min(c1,c2,c3))

