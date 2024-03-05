tup=(1,2,3)
#print(tup[0])
#print(len(tup))
#print(max(tup))
#print(min(tup))
#since it in immutable we cannot add,extend,append,remove data after it is defined
tup=tuple("Tool geel")
print(tup)
#we can change the list into tuple
tup=tuple([4,5,6])
print(type(tup))
#it wont recoganize as tuple it will be counted as a integer
tup=(1)
print(tup)
#to define a single element tuple we add a comma
tup=(1,)
print(tup)
for i in tup:
    print(tup)