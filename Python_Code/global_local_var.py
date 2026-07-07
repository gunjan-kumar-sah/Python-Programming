"""a = 10       # global variable
def something():
 # print(globals())  # prints all global variables
  a = 5          # Local variable
  globals()['a'] = 20
              
  print("inside : ", a)

something()
print("Outside : ", a)"""


x = 20
def update():
  x = 10
  print("Inside function: ",x)

update()
print("Outside function: ", x)  