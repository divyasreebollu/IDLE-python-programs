n = int(input("Enter a number: "))
noofdigits = len(str(n))
square = n**2
lastdigits = square%pow(10,noofdigits)
if lastdigits ==n:
    print("Automorphic".format(n))
else:
    print("Not automorphic".format(n))
