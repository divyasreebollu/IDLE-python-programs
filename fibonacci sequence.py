n= int(input("Enter the Range Number: "))
First = 0
Second = 1
for i in range(0, num):
           if(i <= 1):
                      next = i
           else:
                      next = First + Second
                      First = Second
                      Second = next
           print(next)
