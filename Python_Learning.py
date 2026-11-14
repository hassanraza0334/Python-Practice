# Loops
# Search for a Number X in this Tuple using loop...
num=(1,4,9,16,25,36,49,64,81,100)
X=36
i=0
while i<len(num):
    if (num[i]==X):
        print("Found Ined :",i)
    i+=1
