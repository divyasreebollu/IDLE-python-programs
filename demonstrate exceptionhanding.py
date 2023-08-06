def divide(x,y):
  try:
    result=x/y
  except ZeroDivisionError:
     print("Division by zero")
  else:
    print("result is:",result)
  finally:
     print("executing finally block")
divide(2,1)
divide(2,0)
