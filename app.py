
correct_pin = 1234
PIN = int(input("Enter your PIN:"))
if PIN != correct_pin:
   print("Wrong PIN. Access denied")
else:
   Amount = (int(input(" Enter Amount:")))
   if Amount > 500:
       print("Amount too large. Max is 500.")
   elif 1 <= Amount <= 500:
      print(f"Withdrawing {Amount} ... Done!")
   else:
      print("Invalid Amount.")
total = 0
count = 0
while True:
   numbers = int(input("Enter a number:"))
   if numbers == 0:
      break 
   total += numbers
   count += 1
print(f"You entered {count} numbers. Total is {total}")   



