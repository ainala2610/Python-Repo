class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self.__age = age          # private attribute (note the double underscore)

    def get_age(self):            # public method to access private data
        return self.__age

    def set_age(self, age):       # public method to modify private data
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

# Usage
p = Person("Ajay", 30)
print(p.name)        # ✅ Accessible
print(p.get_age())   # ✅ Accessing private attribute via method

p.set_age(35)        # ✅ Modifying private attribute safely
print(p.get_age())

# print(p.__age)     # ❌ Error: Attribute is private
