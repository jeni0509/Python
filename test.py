srt1="code"
str2="io"
print(srt1,str2,sep=".",end="\t")
print(str2)
#2
a=input("enter a number")
print(a*5)
#3
r=10
x=r**5
r%=5
print(r)
#4
n=25
print(n%24==0 or n%30 ==0 )
#5
a=int(input("Enter a number"))
for i in range(a):
    print(i,end='')
#6
LST=[10,30,40,60]
for i in LST:
    if i == 40:
        break
    else:
        print("40")
#7
LST=[10,30,40,60]
print((10*2)in LST)
print(LST)
print(LST[-1] + LST[1])
