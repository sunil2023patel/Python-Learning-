a={67,78,13,23,29,1,2,3,5}
print(type(a))
a.add(9)
# traversing over set
for _ in a:
    print(_)
# set methods 
# add() adds an element
# clear() removes all the elements
# discard()-removes the specified element
# pop() - removes an random element from the set
# remove() 
a.add(8)
print(a)
a.discard(8)

print(a)
h=a.pop()
print(h)
l={10,20,30,40}
m={20,30,40,50}
n={30,40,4}
print(l.difference(m)) # returns the difference of two sets and returns the set which contains non common element starting elment with the other one
print(l-m)
# l-=m
# print(l)
print(l&m) # returns the set which contains intersection of two sets 
l&=m # updates the set by the intersection of two or more sets 

print(l)
print(n<=m)# returns true if n is subset of m 

## symmetric difference 
s1={4,5,6,7}
s2={5,6,8,9}
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s1| s2) # union of two sets