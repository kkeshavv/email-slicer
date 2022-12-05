a=[]
print('''Type "end" if you are done'''   )
while True:
    
    b=input("type id: ")
    a.append(b)
    if b=="end":
        break
a.remove("end")
print()

for i in a:
    c=i.split('@')
    print("For ",i)
    print()
    print(">>>>>>>user name =",c[0])
    print(">>>>>>>domain name=",c[1].upper())
    print()



