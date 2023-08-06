import math
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while(b!=0):
  temp=b
  b=a%b
  a=temp
  gcd=temp
print("gcd of two numbers:",gcd)  
