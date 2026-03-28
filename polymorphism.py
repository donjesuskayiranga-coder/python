class Dog:
    def speak(self):
        return "woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"


animals = [Dog(), Cat(), Bird()]  

for animal in animals:
    print(animal.speak())
