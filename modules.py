import math
import random
from datetime import datetime
import os

print(math.sqrt(16))
print(math.pi)
print(math.ceil(4.2))#round up 5
print(math.floor(4.9))
print(math.pow(2,3))

print(random.randint(1, 10))
print(random.choice(["a", "b", "c", "d"]))
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.strftime("%d/%m/%Y"))

print(os.getcwd())
os.mkdir("Proper")
print(os.listdir("."))
os.remove("notes.txt")



      
