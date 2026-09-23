class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

animals = [
    Dog("Rex"),
    Cat("Whiskers"),
    Animal("Generic Creature")
]

for animal in animals:
    print(animal.speak())

print(isinstance(Dog("Rex"), Animal))
