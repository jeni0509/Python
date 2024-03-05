#only key used here should have immutable datatype(string,int,tuple) (key:value)
#(0: key trool:value)
D={0:"Trool",1: "geek"}
#traversal in dic
for i in D:
    print(i,D[i]) #only key is printed dic is an unorder not index based
print(D[0])
#adding element
#only uniquie not dupli key is accepted
D[2]="Hello"
print(D)
#delete an element
del D[0]
print(D)
#element =D.pop(0)
#pop function is used here with a KEY value and if we use in list we used use INDEX
#update()
E={0:"Trools",1: "geeks"}
U={2:"Trols",2: "geks"}
E.update(U)
#keys() to return all the keys
#values() to return all values
#items () to return as tupil in list
print(D.values())
print(D.keys())
#to find the key
print(1.in D)
#to find the key
#to find the values is presnt to that value in dic
print("trool" in D.values())