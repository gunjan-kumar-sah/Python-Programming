# Create a private class property named __age:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("GUNJAN", 21)
# print(p1.name)
# print(p1.__age) # This will cause an error


# To access a private property, you can create a getter method:


# class Person:
#   def __init__(self, name, age):
#     self.name= name
#     self.__age = age # Private property

#   def get_age(self):
#     return self.__age

# p1 = Person("GUNJAN", 21)
# print(p1.get_age()) # Output: 21



# Use a setter method to change a private property:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("GUNJAN", 21)
print(p1.get_age())

p1.set_age(22)
print(p1.get_age())