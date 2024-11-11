a=int(input("Enter a number: "))
x=a
res=0
while(a):
    r=a%10
    a=a//10
    res=(res*10)+r
a=x
if(a==res):
    print("Number is Palindrom")
else:
    print("Number is not Palindrom")
