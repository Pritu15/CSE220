def add(a,b):
    return a+b,"Hello",[2,3]

a=int(input())
b=int(input())
s,a,b=add(a,b)
print(s)
print(a)
print(b)

def func(a,*ver):
    print(a)
    print(ver)
    print(type(ver))
    for i in ver:
        print(i)
func(1)
func(1,2,3,4)