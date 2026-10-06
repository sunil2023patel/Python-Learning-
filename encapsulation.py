# Encapsulation (means putting data and code together in one place inside a class)
# it also means hiding internala details of how things work ,and only showing what is needed
# it keeps data safe from being changed by mistake 
# control over what other can change or access
class Factory:
    __name="kia" # public class attribute
    _old=12  #protected
    a=12 # public class attribute
    def __init__(self,type,tyre,color):
        self.type=type # public object attribute
        self.__color=color # private object attribute
        self.tyre=tyre
    def __detail(self):# public method
        print("ur details are:")
Obj=Factory("sedan","MRF","black")
# obj.name="Maruti"
# print(Obj.name)
# print(obj.details())
## __  makes the attributes and methods private form public
# class hello(Factory):
#     print(super().__name)


class Hello:
    __a=12
    @classmethod
    def info(cls):
        print(cls.__a)
obj=Hello()
obj.info()


#Abstraction  
#abstract classes are the classes that contains one or more abstract methods
# a method that is defined but not implemented in the abstract class subclasses must provide the implementation 

from abc import ABC,abstractmethod
class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass

class bike(enforce):
    def enginestart():
        pass
class truck(enforce):
    def enginestart():
        pass
class car(enforce):
    def enginestart():
        pass
obj1=bike()
boj2=car()
obj3=truck()
# Dunder methods

# class aanimal:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"hello my name is {self.name}"
# obj=aanimal("Lion")
# obj2=aanimal("jiraf")
# print(obj2)

class numbers:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
        return self.num+other.num
    def __eq__(self, value):
        return self.num==value.num

num1=numbers(8)
num2=numbers(8)
print(num1==num2)
a=12
print(dir(int))