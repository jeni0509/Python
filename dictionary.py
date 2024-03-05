config={
    "browser":"opera",
    "auto":"google",
    "test":"smoke",
    "log":True

}
print(config.get("auto"))#to get a particular value we add as a dictionary here google will be printed
for conf in config:
    print(conf)
#all the key words will be printed browser,auto,test and log
#in order to get the value in the dictionary
for config1 in config.values():
    print(config1)
#like for in we can also use if in statement here
    if "browser" in config:
        print("exsist")


