def save_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
        print("Note saved!")
def read_notes():
    with open("notes.txt", "r") as file:
        for line in file:print(line.strip()) 
        
while True:
    choice = input("1. Add note 2. Read notes 3. Quit: ")
    if choice == "1":
        note = input("Enter your note: ")
        save_note(note)
    elif choice == "2":
        read_notes()
    elif choice == "3":
        break       
