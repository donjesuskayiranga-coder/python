import random

def guessing_game():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter a number(1-50): "))
            attempts += 1
            if guess > secret:
                print("too high")
            elif guess < secret:
                print("too low")    
            else:
                print(f"Correct! you got it in {attempts} attempts!")
                break
        except ValueError:
            print("Enter a valid number !") 
            
guessing_game()                       

