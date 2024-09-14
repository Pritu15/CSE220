def printinfo(arg1, *vartuple) :
 print("Output is: ")
 print(arg1)
 for var in vartuple :
     print(var)
     
printinfo(10)
printinfo(10,20,30,40,50)

def printInfo1(name,*var) :
    print("Name: ",name)
    if len(var)>0:
        print("Age : ",var[0])
    if len(var)>1 :
        print("CGPA: ",var[1])
    print("-------")
printInfo1("NONE")
printInfo1("Someone",27)
printInfo1("Someone",28,3.95)

