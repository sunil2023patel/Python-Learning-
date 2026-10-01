print("hello how are u")
a=12
# exception error 
# zero division error
# type error adding int and string
# value error
# file not found error

# a=int(input("enter your first number-"))
# b=int(input("enter your second number-"))
# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry an error occured as {err}")
# else:
#     print("no errors occured")
# finally:
#     print("if there are errors or there are no error i will run")
# # print(a/b)
# name=input("enter your name:")
# print(f"hello your name {name}")
age=int(input("enter your age:"))
if age<18:
    raise TypeError("you are not eligible")
print("you are eligible")