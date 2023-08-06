num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
if (num1>num2)and(num1>num3):
  largest=num1
elif (num2>num1)and(num2>num3):
  largest=num2
else:
  largest=num3
print("Largest number:",largest)
a1=min(num1,num2,num3)
a3=max(num1,num2,num3)
a2=(num1+num2+num3)-a1-a3
print("Ascending order:",[a1,a2,a3])
