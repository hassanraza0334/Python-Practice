# Program to find the Greater of 3 Number enter by the User


a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
d=int(input("Enter Fourth Number"))
if(a>=b and a>=c and a>=d):
    print("First Number is Greater than :",a)
elif(b>=a and b>=c and b>=d):
    print("Second Number is Greater than :",b)
elif(c>=a and c>=b and c>=d):    
    print("Third Number is Greater Than :",c)
else:
    print("Fourth number is greater than :",d)
    