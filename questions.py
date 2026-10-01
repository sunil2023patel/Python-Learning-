l=[9,8,4,-3,2,-1,-19]
pos=[]
neg=[]
for _ in l:
    if _ >=0:
        pos.append(_)
    else:
        neg.append(_)
print(pos)
print(neg)
# second largest element
lar=float('-inf')
slar=float('-inf')
for _ in l:
    if(lar<_):
        slar=lar
        lar=_
    elif slar<_:
        slar=_
print(f"larget value {lar} and second largest value is {slar}")