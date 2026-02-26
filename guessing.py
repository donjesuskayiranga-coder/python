number = 67

attempt = 0

for i in range(5):
     guess = float(input("Guess the number:"))
     if guess > number:  
           print("Too high") 
     elif guess < number:
            print("Too low")       
     attempt += 1
     if  number == guess:
       print(f"correct! You got it in {attempt} attempts")
       break
     if attempt == 5:

      print(f"Game Over! The number was {number}")
     
