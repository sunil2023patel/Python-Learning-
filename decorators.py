def extragreeting(func):
    def wrapper(*args,**kwargs):
        print("hello form NYC team")
        func(*args,**kwargs)
        print("thankyou visit again0")
 
    return wrapper 

# @extragreeting
# def greeting():
#     print("good morning")
# greeting()


def decorate(func):
    def wrapper():
        print("welcome to our portal")
        func()
        print("Thank you for visiting")
    return wrapper
        
@decorate
def content():
    print("This is the content of my website or project")
content()


# def addtion(*args):
#     s=0
#     for i in args:
#         s+=i

#     return s
# print(addtion(39,40,59,5,6,7,8))
# args ek tuple create krta hai 
# kwargs ek dictionary create krta hai key:value
def info(**kwargs):
    return kwargs
print(info(name="akarsh",age=24,profession="data scientist"))
@extragreeting
def  add(a,b,c):
    print(a+b+c)
add(9,0,8)
def sub(func):
    def wrapper(*args,**kargs):
        print("Hello")
        func(*args,**kargs)
        print("how are u")
    return wrapper

@sub
def sub(a,b):
    print(a-b)
sub(3,5)



a=23 # ternary operation 

print("even numbers") if a%2==0 else print("odd number")
# *****COMPREHENSION*****
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[i for i in a if i%2==0]
# for i in a :
#     if i%2==0:
#         b.append(i)
print(b)
squared={x:x**2 for x in range(5)}
unique={x&1 for x in range(10)}
print(squared)
print(unique)


# Lambda expressions
# def check(a):
#     if a%2==0:
#         print("even number")
#     else:
#         print("odd number")


# check(6)
check=lambda x: "even number" if x%2==0 else "odd number"
print(check(12))
add=lambda *args: args
print(add(9,8,7))
k=["sarthak","harsh","vedant","akarsh"]
for i in k:
    print(len(i))
length=list(map(len,k))
print(length)

temp=[0,20,30,35]
def converter(a):
    far=(a*(9/5))+32
    return far
temp_f=list(map(lambda x:(x*9/5)+32,temp))
print(temp_f)
#filter
m=[45,66,77,88,98,23,1,2,49]
passed=list(filter(lambda x:x>=40,m))
print(passed)

name=['sarthak',"akarsh","harsh","vedant"]
marks=[12,34,56,78]
result=list(zip(name,marks))
print(result)