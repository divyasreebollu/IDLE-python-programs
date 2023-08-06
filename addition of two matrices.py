m=int(input("Number of rows in Matrix-A,m="))
n=int(input("Number of columns in Matrix-A,n="))
p=int(input("Number of rows in Matrix-B,p="))
q=int(input("Number of columns in Matrix-B,q="))
if(m==p and n==q):
  a=[]
  b=[]
  print("Enter values for Matrix-A")
  for i in range(m):
    matrix1=[]
    for j in range(n):
      print("Entry of row:{} column:{}".format(i+1,j+1))
      matrix1.append(int(input()))
    a.append(matrix1)
  print("Enter values of Matrix-B")
  for i in range(p):
    matrix2=[]
    for j in range(q):
      print("Entry of row:{} column:{}".format(i+1,j+1))
      matrix2.append(int(input()))
    b.append(matrix2)
  print("Matrix-A={}".format(a))
  print("Matrix-B={}".format(b))
  sum=a.copy()
  for i in range(m):
    for j in range(n):
      sum[i][j]=a[i][j]+b[i][j]
  print("Addition of two matrices={}".format(sum))
else:
  print("Addition not possible")
