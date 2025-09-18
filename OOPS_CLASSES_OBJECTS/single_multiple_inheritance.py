# Single inheritance example:

# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Usage
dog = Dog()
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog


# Multiple Inheritance example:

# Parent class 1
class Flyer:
    def fly(self):
        print("Flying high")

# Parent class 2
class Swimmer:
    def swim(self):
        print("Swimming fast")

# Child class
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

# Usage
duck = Duck()
duck.fly()    # Inherited from Flyer
duck.swim()   # Inherited from Swimmer
duck.quack()  # Defined in Duck
