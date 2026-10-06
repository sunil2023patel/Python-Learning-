# a=10 imperative 
# b=9
# print(a+b)
# def add(a,b): functional 
#     print(a+b)
# add(9,8)
# add(4,8)
# Oops provides you security 
class Car:
    a=12 # attribure
    def hello(): # method
        print("how are u")
# you can access attributes and methods after accessing the class
print(Car.a) # accessing attributes 
Car.hello() # acessing methods
# objects
# class Bags:
#     name="NOtYourCollege"
#     def details(self):
#         print("hello this is a company who creates bags ")
# reebok=Bags()
# print(reebok.name)
# reebok.details()
# class Bags:
#     def __init__(self,material,zip,pockets):
#         self.material=material
#         self.zip=zip
#         self.pockets=pockets
#         print("How are u ")
# # Bags() # whenever u call a class contructor is called everytime
# reebok=Bags("leather",3,2)
# campus=Bags("polyester",4,2)
# print(campus.material)
# class Animal:
#     a=12
#     def __init__(self,name):
#         self.name=name # instance/objects attributes
#     def hello(self): # object/instance method
#         print(f"how are you my name is {self.name}")
#     @classmethod # decorators
#     def details(cls): # class method captures the location of class
#         print(f"how are you my name is {cls.a} ")
#     @staticmethod
#     def speak(): # this is a static method and it will not target any location 
#         print("hello how are u i m a static method")
# obj=Animal("lion")
# print(obj.name)
# obj.hello()
# obj.details()
# obj.speak()
##### INHERITANCE ######
# class Animal: # parent class
#     a=40
#     def __init__(self,name):
#         self.name=name
#     def details(self):
#         print(f"hello Your name is {self.name}")
# class Humans(Animal):# child class
#     pass
# obj1=Animal("lion")
# obj2=Humans("harsh")
# obj2.details()
# print(obj2.a)
# # you child class objects has all the powers to access the attributes and methods of parent class

# class BagFactory:
#     def __init__(self,material,zips,pockets):
#         self.material=material
#         self.zips=zips
#         self.pockets=pockets
#     def details(self):
#         print("your bag details are:")
#         print(self.material)
#         print(self.zips)
#         print(self.pockets)
# class Reebok(BagFactory):
#     def __init__(self, material, zips, pockets,color):
#         super().__init__(material, zips, pockets)
#         self.color=color
#     def details(self):
#         print(self.color)
#         return super().details()

# class campus(Reebok): # multilevel inheritance
#     def __init__(self, material, zips, pockets, color,size):
#         super().__init__(material, zips, pockets, color)
#         self.size=size
# bag2=Reebok("polyster",4,6,"red")

# print(bag2.color)
# bag1=BagFactory("leather",4,5)
# class animal:
#     def __init__(self,name):
#         self.name=name
# class humans:
#     def __init__(self,id):
#         self.id=id
# class robots(humans,animal): # multiple inheritance
#     def __init__(self, id,name):
#        humans.__init__(id)
#        animal.__init__(name)
# robo=robots(12,"akarsh")
##### Polymorphism #### having many forms

# def hello():
#     print("how are u ")
# def hello(): this will overwrite
#     print("what are u doing")

# hello() 
class animal:
    def speak(self):
        print("animal can spaeak")

class humans:
    def speak(self):
        print("we are humans we can speak")
obj=animal()
obj2=humans()
obj.speak()
obj2.speak()
# method overriding (we need inheritance )
class Animal:
    a=12
    def __init__(self,name):
        self.name=name
    def details(self):
        print(f"your name is {self.name}")
class Humans(Animal):
    b=12
    def details(self):
        super().details()
        print(f"your info is {self.name} and this is all we have")
obj=Humans("harsh")
obj.details()
# when we are doing inheritance and parent and child classes have same method name so the child class method will override your parent class method 

# method overloading python does not support traditional method overloading and if u define multiple methods with the same name the last definition will overwrite all the preceding ones
# however we can achieve indirectly using these methods 
# 1.using defalult arguments
# 2.using variable length argument *args and **kwargs 
# 3.using type module but still u need to handle the runtime logic normally
# 4. using multipledispatch libraray

class hello:
    def speak(self,a):
        print(f"how are you")
    def speak(self,a,b):
        print("how are u ")
class stable:
    a=12
print(stable.a)

