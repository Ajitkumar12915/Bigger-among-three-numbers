a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
max=a
if max<b:
    max=b
    if max<c:
        max=c
        print('Bigger=',max)