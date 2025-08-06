class Animal:
    def speak(self):
        return "Sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Bark
animal_sound(Cat())  # Meow
