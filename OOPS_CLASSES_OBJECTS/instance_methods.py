class dog:
       def __init__(self,name,age):
              self.NAME= name
              self.age=age
         
    # defining the method
       def bark(self):   # method
              print(f"{self.NAME} says woof and its age is {self.age}")

dog2=dog("TIGER",4) 
dog2.bark()   # calling the method
