#python is completed by giving the functions
config={
    "browser":"opera",
    "auto":"google",
    "test":"smoke",
    "log":True

}
def getdictionaryvalue(key):
    return config.get(key)
print(getdictionaryvalue("test"))

def getdictionaryvalue(key="browser"):
    return config.get(key)
print(getdictionaryvalue())
#here we can passing in default argument without passing any parameter in print in this o/p = opera


def getdictionaryvalue(key="browser"):
    return config.get(key)
print(getdictionaryvalue("test"))
#here the  parameter takes up the priority in print in this o/p = opera