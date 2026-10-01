a="hello word!"
b="%"
print(a)
print(ord(b))
print(a[0])
# string slicing 
# string[start:stop:step] stop is excluded
print(a[0:4:2])
v=a[0:4:2]
print(v)
z="College"
print(z[3:6])
print(z[::-2])
#type conversion 
p=12.4
print(type(p))
print(type(int(p)))
# you can convert string if it holds valid integers 
# you can convert float values to int 
a="12.4"
a=float(a)
print(type(a))
# 7 falsy values
#false,0,0.0,"",[],(),