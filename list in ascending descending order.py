a=input("Enter list:")
b=a.split(" ")
for i in range(len(b)):
  b[i]=int(b[i])
list=sorted(b)
print(list)
list.sort(reverse=True)
print(list)
