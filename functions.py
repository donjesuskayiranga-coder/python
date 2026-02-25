#def get():
#print("Hello! welcome to Python.")
#get()
#def greet(name):
#   print(f"Hello {name}! Welcome to Python.")
#greet("Jean")
#def add(number1, number2):
#   print(number1 + number2)
#  add(5, 3)
# add(10, 20)
#def add(number1, number2):
 #   return number1 + number2
#result = add(5,3)
#print(result)
#def greet(name="stranger"):
 #   print(f"Hello {name}!")
#greet("Jean")
#greet()
def add(a, b):
    return a + b
def is_even(number):
    if number % 2 == 0:
     return True
    else:
        return False
    
def grade(score):
   if score >= 90:
      return "A"
   elif score >= 80:
     return "B"
   elif score >= 70:
      return "C"
   elif score >= 60:
    return "D"
   else:
      return "F"
   
result = float(input("Enter a number"))
result2 = float(input("Enter another number:"))
result3 = add(result, result2)
print(result3)

number1 = float(input("Enter a number:"))
print(is_even(number1))

score1 = float(input("Enter ur Score:"))
print(grade(score1))






    









