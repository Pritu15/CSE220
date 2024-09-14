i=1
while i<10:
    print(i)
    i=i+1
a=[1,2,3,4,5]
print("Printing the full list: ")

for i in a:
    print(i)
print("Printing using range")
for i in range(1,5,2):
    print(i)
b=list(range(1,5))
for i in b:
    print(i);
    
names=['Pritu','partho','joy']

for i in range(len(names)):
    print(names[i])
