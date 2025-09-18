# An instance of a class. It holds actual data and can use the class's methods.

class dog:
     
## Defining constructor
     def __init__(self,name):
            self.NAME=name
        #   self.age=age

## Create objects which use class methods by passing variables

dog1=dog("RAGHU")  # dog1 is an object which is calling class dog
print(dog1.NAME)
