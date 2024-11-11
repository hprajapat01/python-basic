num=int(input("Enter a number: "))
def fect(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

res=fect(num)
print(res)
