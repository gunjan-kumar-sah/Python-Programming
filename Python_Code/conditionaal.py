# num = int(input("Enter your number:-"))
# if(num % 2 == 0):
#   print("Even")
# else:
#   print("Odd")

a = int(input("Enter first numer:-"))
b = int(input("Enter second numer:-"))
c = int(input("Enter third numer:-"))
if(a>b and a>c):
  print("First number is largest", a)
elif(b>c):
  print("Second number s largest", b)
else:
  print("Third number is Largest", c)