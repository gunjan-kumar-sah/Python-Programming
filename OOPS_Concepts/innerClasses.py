class Outer:
  def __init__(self):
    self.name = "Outer Class"
    # self.__age = 21
  class Inner:
    def __init__(self):
      self.name = "Inner Class"  

    def display(self):
      print("This is an inner class method")

outer = Outer()
print(outer.name)

# print(outer.Inner().name)  # Accessing the inner class name
# outer.Inner().display()   # Calling the inner class method

inner = outer.Inner()   # Calling the inner class method
inner.display()