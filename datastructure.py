# some data structures list,tuple,dictionary,set
a=[1,2,3,4,'sunil','shikha','sharanya','bhoomi','vashundhara']
print(type(a))
# ORDERED NATURE YOU CAN ACCESS ANY ELEMENT AT ANY POINT OF TIME
# IT CAN STORE DUPLICATES AND WE CAN CHANGE THE VALUES 
s="sunil" # strings are immumatable in nature u can not change characters once it is created
# s[0]='o'
print(s) 
# TRAVERSING OVER LIST
print(a)
# traversing over values 
for i in a:
    print(i,end=" ")
# traversing on index
print('\n')
print(*a)
print('\n')
for i in range(len(a)):
    print(a[i])

b=[10,20,30,40,50]
# CRUD 
# adds a value to the last spot
# create new element
b.append(90)
b.append("sunil")
b.append(True)
print(b)
b.insert(2,40) # addsvalue in the middle 
print(b)
l=[10,20,30,40,55,20,50]

item=l.pop(4)# remove the element at particular index l.pop(index) and return the removed item
print(item)
print(l)
# remove method l.remove(value) and does not return anything
l.remove(20)
print(l)

l.sort(reverse=True)
print(l)

# Tuple
# immutable list u can not change any element
l.append(20)
tup=tuple(l)
print(tup)
print(type(tup))
print(tup[-1])
print(tup.index(30))
print(tup.count(20))
def students():
    return 'sunil',900,'akarsh@gmail.com'
a=56,4,3,4
name,score,gmail=students()
print(gmail)


