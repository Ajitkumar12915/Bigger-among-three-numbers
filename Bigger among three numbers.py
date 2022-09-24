a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
max=a
if max<b:
    max=b
    if max<c:
        max=c
        print('Bigger=',max)
        # another method for same problem is given below.
      a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if a>b:
    if a>c:
        print(a)
       else:
        if b>c:
            print(b)
            else:
                print(c)
        
