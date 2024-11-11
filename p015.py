num=int(input("Enter a Number: "))
count=0
a=num
res=0
while(num):
    count=count+1
    num=num//10
print(count)
num=a
while(num):
    r=num%10
    num=num//10
    res=res+(r**count)
if(res==a):
    print("YES")
else:
    print("NO")
