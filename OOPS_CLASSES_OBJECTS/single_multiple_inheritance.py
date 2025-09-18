# Single inheritance example:

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} barks.")

# Usage
dog = Dog("Buddy", "Labrador")
dog.speak()  # Inherited method
dog.bark()   # Child method

##### Multiple Inheritance example:

# Parent class 1
class Flyer:
    def __init__(self, wing_span):
        self.wing_span = wing_span

    def fly(self):
        print(f"Flying with a wingspan of {self.wing_span} meters.")

# Parent class 2
class Swimmer:
    def __init__(self, swim_speed):
        self.swim_speed = swim_speed

    def swim(self):
        print(f"Swimming at {self.swim_speed} km/h.")

# Child class
class Duck(Flyer, Swimmer):
    def __init__(self, name, wing_span, swim_speed):
        Flyer.__init__(self, wing_span)
        Swimmer.__init__(self, swim_speed)
        self.name = name

    def quack(self):
        print(f"{self.name} says quack!")

# Usage
duck = Duck("Daffy", 1.2, 5)
duck.fly()
duck.swim()
duck.quack()

