"""
def square(num):
  return num* num

def cube(num):
  return num*num*num

value = 5
result = square(value)
print(result)"""



# def square(num):
#   return num*num


# def cube(num):
#   return num*num*num

# def operate(n, operation):
#   for i in n:
#     result = operation(i)
#     print(result)

# n = [5,6,7,8]
# operate(n,cube)




def square(num):
  return num*num

def cube(num):
  return num*num*num  

def operate(nums, operation):

  for i in nums:
   result = operation(i)
   print(result)

nums = [1,2,3,4,5,6]
operate(nums, square)



"""def square(num):
  return num*num

def cubes(num):
  return num*num*num

def operate(nums,operation):
  for i in nums:
   result = operation(i)
   print(result)

nums = [1,2,3,4,5,6]
operate(nums,square)"""

