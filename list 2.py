lst = [1, 2, 3,1]
# lst.append(4)#it will insert this value in the list
# print(lst)
# lst.insert(1,4)
# print(lst)
#lst.extend([4,5,6])
#print(lst)
#it will be added at the end when we use append we will get a o/p = [1,2,3,[4,5,6]] it will be appended as a
#nested list thats why we dont use append
#lst.remove(1)
#print(lst)
#it will remove the vlaue from the list only the first occurance will be removed
#pop()to remove the element from index
lst.pop(3)
print(lst)
element =lst.pop(2)
print(lst)
print(element)
#ascending order sort
lst.sort()
print(lst)
#descending order
lst.sort(reverse=True)
print(lst)
#list function will give the seprate the element of string as element of list[0,1 etc.,]
lst=list("trool geek")
print(lst)
