
f=open("myfile","a")
f.write("My name is harsh and i am a BCA student")
f.close()

f=open("myfile","r")
print(f.read())
f.close()

import os
os.remove("myfile")

f=open("myfile",'r')



