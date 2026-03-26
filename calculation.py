
import math

try:
 num1 = float(input("Enter a number: "))
 num2 = float(input("Enter another:"))
 operation = input("enter operation(+,-,*,/)")

 if operation == "+":
    result = num1 + num2
    print(f"result :{result}")
    if result < 0:
       print("no squareroot of negative number")
    else:
     print(f"squareroot : {math.sqrt(result)}")

 elif operation == "-":
    result = num1 - num2
    print(f"result: {result}")
    if result < 0:
       print("no squareroot or negative number")
    else:
     print(f"squareroot : {math.sqrt(result)}")
     
 elif operation == "*":
    result = num1 * num2
    print(f"result: {result}")
    if result < 0:
       print("no squareroot or negative number")
    else:
     print(f"squareroot : {math.sqrt(result)}")
    
 elif operation == "/":
    result = num1 / num2
    print(f"result: {result}")
    if result < 0:
       print("no squareroot or negative number")
    else:
     print(f"squareroot : {math.sqrt(result)}")
    
except ZeroDivisionError:
   print("you can't divide by zero enter another number!😂") 

except ValueError:
   print("Enter a valid number 👌")   

finally:
   print("calculation complete😍")




