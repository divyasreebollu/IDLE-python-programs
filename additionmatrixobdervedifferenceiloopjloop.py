m=int(input("Enter no of rows: "))
n=int(input("Enter no of columns: "))
a=[]
print("values for A")
for i in range(m):
    l1=[]
    for j in range(n):
        ele1=int(input("row:{} column:{} :".format(i,j)))
        l1.append(ele1)
    a.append(l1)
print(a)
p=int(input("Enter no of rows: "))
q=int(input("Enter no of columns: "))
b=[]
print("values for B")
for i in range(p):
    for j in range(q):
        l2=[]
        ele2=int(input("row:{} column:{} :".format(i,j)))
        l2.append(ele2)
    b.append(l2)
print(b)
