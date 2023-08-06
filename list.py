li = []
n = int(input("Enter the size of the list: "))
for val in range(n):
    ele = int(input("Enter the {} element: ".format(val)))
    li.append(ele)
    print("The element in the list are : ")
for val in li:
    print(val,end=' ')
