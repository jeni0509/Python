a="tool geek"
print(a[0:5])#only slice from 0 to 4 elements
print(a[:])
print(a[5:])
print(a[:5])
#no error will come if you say in upper limit to be higher
print(a[0:67])
#step value it will skip that particular index and show the other
print(a[0:10:2])
#step value in reverse it will skip in reverse order upper should be lower than lower it will print in reverse
print(a[10:0:-1])