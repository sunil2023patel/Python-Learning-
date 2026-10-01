dic={1:10,2:20,3:30,4:40}
# vanilla python 
print(type(dic))
dic[50]= 500 # create new key value pair
print(dic)
print(dic[3]) # reading a value
dic[1]=100 # update a key value that already exist 

print(dic)
# methods approach

q=dic.fromkeys([1,2,4,5],50)
print(dic.get(2)) # using method/function
print(q)
print(dic.items())
print(dic.keys())
print(dic.values())
print(dic)
# print(dic.pop(1)) # deletes particular key value pair and returns the deleted value
# dic.popitem() # removes the last item 
print(dic.setdefault(3,3000)) # returns the value and if it does not exist create new key value pair 
dic.update({8:900}) # update and create  new key value pair 

print(dic)

#traversing
d={10:100,20:200,30:300,40:400,50:500}
for i in d:
    print(i,end=" ")

