d1={'a':10,'b':20,'c':30}
d2={'c':40,'e':50,'f':60}
# # d1.update(d2)
# # print(d1)
for keys in d2:
    if keys in d1.keys():
        d1[keys]+=d2[keys]
    else:
        d1[keys]=d2[keys]
    
print(d1)
# l=['a','b','a','c','b','a']
# dic={}
# for i in l:
#     if i in dic.keys():
#         dic[i]+=1
#     else:
#         dic[i]=1
# print(dic)
# print(dic.keys())

 

