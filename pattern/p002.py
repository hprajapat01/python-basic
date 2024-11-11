n=int(input("Enter the number of rows: "))
x=1
for i in range(n):
    for j in range(x,n):
        print(end=" ")
    x=x+1
    for k in range(i+1):
        print("* ",end="")
    print("\n")
