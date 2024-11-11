n=int(input("Enter range: "))
f=0
s=1
print(f)
print(s)
for i in range(3,n+1):
    t=f+s
    f=s
    s=t
    print(t)
    
