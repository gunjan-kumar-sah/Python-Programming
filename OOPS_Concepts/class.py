#class creation
class Vehicle:
  color = "White"  #attribute
  petrolOrDiesel = "Petrol"  #attribute
  mileage = "39"  #attribute

  def start():
      print("Vehicle is starting")  #method

#object creation
car = Vehicle()
car.color = "Pink"  #changing the attribute value
print(car.color)

bike = Vehicle()
print(bike.mileage)

aeroplane = Vehicle()
print(aeroplane.petrolOrDiesel)
print(aeroplane.color)

print(car.start())
