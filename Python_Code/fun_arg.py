# def add(num1,num2):
  # print("sum = ", num1+num2)
  # add(4,5)


# def add(num1,num2):     #default argument
#   return num1+num2

# def add(num1, *num2):   # variable length argument
#   # print(num1)
#   # print(num2)
#   sum = num1
#   for n in num2:
#     sum += n
#   return sum

# result = add(3,9,6,7)
# print(result)

def person(name,**kwlarge):
  print("Name:", name)
  # print("Age:", age)
  # print(kwlarge)
  for k,v in kwlarge.items():
    print(k, ":", v)


# person("Gunjan",20)
# person(age = 20, name = "Gunjan")
person(name = "Gunjan", age = 20, loc = "BUxar", tech = "Python")    #keyword argument