"""Create a class laptop  with attributes: brand, RAM, price. Create 2 objects 
with different values and print the attributes of both objects."""

class laptop:
  brand = "HP"
  RAM = "8GM"
  price = "50,000"

obj1 = laptop()
obj1.brand = "Dell"
obj1.RAM = "8GB"
obj1.price = "75,000"
print("Laptop 1 brand is: ", obj1.brand)
print("Laptop 1 Price is: ", obj1.price)
print("Laptop 1 RAM is: ", obj1.RAM)

obj2 = laptop()
obj2.brand = "Macbook"
obj2.RAM = "16GB"
obj2.price = "1,00,00" 
print("Laptop 2 brand is: ", obj2.brand)
print("Laptop 2 RAM is: ", obj2.RAM)
print("Laptop 2 price is: ", obj2.price)