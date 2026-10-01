# name="sunil"
# age=20
# print(f"hii my name is {name} and my age is {age}")
# print("hii my name is",name,"and my age is",age)
# a=float(input("what is your age!"))
# #arithmatic operators
# # numbers-int,float,complex
# #(+,-,/,//,*,%,**) 
# a=45
# print(a//4)
# '''
# () bracket
# ** power
# * / // % multiplication division floor division remainder
# + - addition and substraction'''
# #comparision operators
# #(==,>,<,<=,>=,!=)
# if True:
#     print("hello how are you !!")


#some problems
# # ask gender and give greetings
# que=input("enter your gender M/F:")
# if que=='M':
#     print("Good Morning sir!!")
# else:
#     print("Good Morning Ma'am")
# # find if a year is a leap year or not 
# yr=int(input("enter a year "))
# if yr%100==0:
#     if yr%400==0:
#         print(f"{yr} is a leap year")
#     else:
#         print(f"{yr} is not a leap year")
# else:
#     if(yr%4==0):
#         print(f"{yr} is a leap year")
#     else:
#         print(f"{yr} is not a leap year")
# # loops 
# # ranges 10-100 range(10,101,1)
# for _ in range(46):
#     print(_);
p=list(range(101))
print(p)
# range(46)
for _ in range(6):
    print("hello i love u ")
# n=int(input("please enter a number"))
# for  i in range(n,n*10+1,n):
#     print(i)
a="Students"
for i in range(len(a)):
    print(f"{i}:{a[i]}")
n=int(input("please tell your number"))
for i in range(n,0,-1):
    print(i)
s="P@#yn26at^&i5ve"
print(s[::-1])
dig=0
char=0
spchar=0
for i in s:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(ord("A"))