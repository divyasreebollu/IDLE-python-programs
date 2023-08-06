low = int(input ("Please, Enter the Lowest Range Value: "))  
high = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for i in range (low, high + 1):  
    if i > 1:  
        for j in range (2, i):  
            if (i % j) == 0:  
                break  
        else:  
            print (i)  
