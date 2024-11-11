a=int(input("Enter the number of units: "))
amt=0
if(a<=100):
    amt=0
    print("Charge is: ",amt)
elif(a>100 and a<=200):
    amt=(a-100)*5
    print("Charge is: ",amt)
else:
    amt=500+(a-200)*10
    print("Charge is: ",amt)
