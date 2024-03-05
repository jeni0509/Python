#Jump statement when we need to skip a iteration and also to come out of while loop we use this
for i in range(10):
    if i ==5:
        continue
    print(i)
#continue : it will skip that particlar iteration it will only skip functions after continue


for i in range(10):
    if i ==5:
        break
    print(i)
#break: it will come out of the loop after break

#else clause:
for i in range(10):
    print(i)
else:
    print("Else clause is executed")
#else clause is executed only when the loop is completed without any intruption
for i in range(10):
    if i==5:
        break
    print(i)
else:
    print("Else clause is executed")

#if else clause if broke because of any  break statment it wont be printed