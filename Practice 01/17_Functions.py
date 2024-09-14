def printme(str) :
    print(str)
    return
# printme(str="MY STRING")

def printInfo(name,age):
    print("Name: ",name)
    print("Age ",age)
    return
# printInfo(age=50,name="miki")

def printInfo1(name,age=35):
    print("Name: ",name)
    print("Age ",age)
    return
printInfo1("Pritu");
printInfo1("PRitu",50)