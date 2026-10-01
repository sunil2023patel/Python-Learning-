def hello():
    print("hello! how are u")
def addition(a,b): # here it is parameter
    return a+b
hello()
# parameters are the values you accept while calling the function
# arguments are the values you provide to parameters while calling the function
sum=addition(9,6) # here it is argument
print(sum)
def reverse(num):
    copy=num
    rev=0;
    while copy>0:
        rev=rev*10+copy%10
        copy//=10
    return rev
givereverse=reverse(12342398)
print(givereverse)
# positional argument
def add(a,b,c):
    print(a+b+c)
add(5,6,8)
# default argument - once you have provided the default argument you can not give normal parameter to the function it will only accept default parameters after that 
def add1(a,b,c=18):
    print(a+b+c)
add1(5,6)
# keyword argument 
def sub(a,b):
    print(b-a)
sub(b=8,a=9)