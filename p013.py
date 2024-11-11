a=int(input("Enter a number: "))
i=2
flag=0
while(i<a):
    if(a%i==0):
        flag=1
    i=i+1
if(flag==0):
    print("Number is Prime")
else:
    print("Number is Not Prime")
