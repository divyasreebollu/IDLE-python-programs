m=int(input("Enter no of rows: "))
n=int(input("Enter no of columns: "))
a=[]
print("values for A")
for i in range(m):
    for j in range(n):
        l1=[]
        ele=int(input("row:{} column:{} :".format(i,j)))
        l1.append(ele)
    a.append(l1)
print(a)

