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
print(grade(score1)
      )
#listing methods
names = ["Jean", "Alice"]
names.append("Bob") #adds to the end
names.insert(1, "Mary") # adds to position 1
#removing items:
names = ["Jean", "Alice","Bob", "Alice"]
names.remove("Alice") #remove the first occurrence of Alice
names.pop() #removes last item
names.pop(0)
numbers = [3,1,4,1,5,9,2,6]
print(len(numbers)) # how many items
print(sum(numbers))
print(min(numbers))
print(max(numbers))
numbers.sort()
numbers.reverse()
print(numbers.count(1))
#looping through a list
names = ["Jean", "Alice","Bob"]
for name in names:
   print(f"Hello {name}!")
if "jean" in names:
   print("Jean exists")
   #getting part of list
numbers = [3,1,4,1,5,9,2,6]
print(numbers[1:4])
print(numbers[:3]) #from index 0 to 2
print(numbers[4:]) #from index 4 to end
print(numbers[::2]) #[1,3,5,7] - every 2 steps
#nested lists
students = [
   ["Jean", 85],
   ["Alice",92],
   ["Bob",78]
]
print(students[0])
print(students[0][0])
print(students[0][1])
numbers2 = []
for number in range(5):
   numbers1 = float(input("Enter a number"))
   numbers2.append(numbers1)
print(numbers2)
print(max(numbers2))
print(min(numbers2))
print(sum(numbers2))
print(sum(numbers2)/len(numbers2))
num = float(input("Enter a number:"))
if  num in numbers2:
   print("Found!")
else:
   print("Not Found!")
   #dictionaries
   #dictionary - access by name
person = {"name": "Jean" , "age": 20, "city": "Kigali"}
print(person["name"])
#format is "Key": value
#dictionary methods
print(person.keys())
print(person.values())
print(person.items())
print(len(person))
students = {
   "Jean":{"age":20, "grade":"A"},
   "Alice": {"age":22, "grade": "B"},
   "Bob": { "age": 19, "grade": "C"}
}
print(students["Jean"])
print(students["Jean"]["grade"])
print(students["Alice"]["age"])
student = {"name":"KAYIRANGA",
            "age":17, "grade": "A", 
            "city":"Kigali", }
for key ,value in student.items():
   print(f"{key}: {value}")
new_city = input("Enter a new city:")
student["city"] = new_city
student["score"] = 95
student.pop("age")
print(student)
#string Methods
#case methods:
name = "jean kayiranga"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
#stripping whitespace:
name ="    Jean   "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
# Finding and replacing:
sentence = "I love Python and Python is great"
print(sentence.find("Python"))
print(sentence.count("Python"))
print(sentence.replace("Python", "coding"))
name = "Jean123"
print(name.isalpha())
print(name.isnumeric())
print(name.isalnum())
age = "20"
print(age.isnumeric()) #True -all numbers
#splitting and joining:
sentence = " I love Python"
words = sentence.split(" ")
print(words)  #["I", "love", "Python"]
words = ["I", "love", "Python"]
sentence = " ".join(words) #joins with space
print(sentence) # " I love Python"
email = "jean@gmail.com"
print(email.startswith("jean")) #True
print(email.endswith(".com")) #True
print(email.endswith(".org")) #false
#multiline Strings
message = """"
Hello Jean,
Welcome to Python.
keep Coding every day!
"""
print(message)
names = input("Enter ur full names:")
print(names.upper())
print(names.title())
print(len(names))
print(names.replace(" ", ""))
print(names.lower().startswith("k"))
words = names.split(" ")
print(words)
#*args: accept any number of arguments
def add(*args):
   total = 0
   for number in args:
      total+= number
      return total
print(add(1,2))
print(add(1,2,3)) 
print(add(1,2,3,4,5))
#**kwargs: accept Any Number of keywords Arguments
def print_info(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}: {value}")
print_info(name = "Jean", age=20, city = "Kigali")   
def describe(title, *args, **kwargs):
   print(f"Title: {title}")
   print(f"Items: {args}")
   print(f"Details: {kwargs}")
describe("Student", "math", "Science", name= "Jean", age=20)
#scope
#global scope
message = "Hello!"
def greet():
   print(message)
greet()
print(message)
#global keyword
#used fro changing a global variable from inside the function
count = 0
def increment():
   global count
   count += 1
   increment()
   increment()
   print(count)
 #lambda functions
 #is a tiny function written in one line 
square = lambda x: x * x
print(square(5))
add = lambda a, b: a + b
print(add(3, 4))
students = [
   {"name": "Jean", "score": 85},
   {"name":"Alice", "score": 92},
   {"name": "Bob", "Score": 78}
]
sorted_students = sorted(students, key=lambda s: s["score"])
for student in sorted_students:
   print(f"{student["name"]}: {student["score"]}")
   def countdown(n):
      if n == 0:
         print("Done!")
         return
      print(n)
      countdown(n - 1)
countdown(5)
#return with nothing after it, it means stop the function and go back
def factorial(n):
   if n == 1:
      return 1
   return n * factorial(n -1)
print(factorial(5)) 
def total(*numbers):
   sum = 0
   for number in numbers:
      sum += number
   return sum
print(total(1,2,3,4))
print(total(2,4))
def describe(**kwargs):
   for key, value in kwargs.items():
      print(f"{key}:{value}")
describe(name="KAYIRANGA", email= "donjesuskayiranga@gmail.com" , grade= "A")
def factori(n):
   if n == 1:
    return 1
   return n * factori(n - 1)
print(factori(8))
#file handling
file = open("filename.txt", "mode")

#writing file
file = open("names.txt", "w")
file.write("Jean\n")
file.write("Alice\n")
file.write("Bob\n")
file.close()

with open("names.txt", "w") as file:
   file.write("Jean\n")
   file.write("Alice\n")
   file.write("Bob\n")

   with open("names.txt", "r") as file:
      content = file.read()
      print(content)

      # Read all lines into a list
with open("names.txt", "r") as file:
   lines = file.readlines()
   print(lines)

   # Loop through lines
   with open("names.txt", "r") as file:
      for line in file:
         print(line.strip()) #strip removes the \n


         #Appending to a file
         with open("names.txt" , "a") as file:
            file.write("David\n")
            file.write("Mary\n")
            #check if a file exists
            import os
            if os.path.exists("names.txt"):
               print("File exists!")
            else:
               print("File not found!")
               









    






























































   











   












    









