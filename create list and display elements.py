n=int(input("Enter the size of the list:"))
l=[]
for i in range(0,n):
  a=int(input("Enter the {} element:".format(i)))
  l.append(a)
print("The elements in the list are:")
for j in l:
  print(j,end=" ")
  
