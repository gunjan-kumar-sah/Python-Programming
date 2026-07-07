"""Map function using function"""
# nums = [4,2,9,5,1,8,6]
# def double_it(n):
#   return n*2
# evens = list(filter(lambda n : n % 2 == 0,nums))
# double = list(map(double_it,evens))
# print("Even value",evens)
# print("double value",double)


"""Map funtion using Lambda Function"""
# nums = [4,2,9,1,8,6,5]

# # double_it = lambda n: n*2
# evens = list(filter(lambda n : n%2 == 0,nums))
# # double = list(map(double_it,evens))
# double = list(map(lambda n: n*2,evens))

# print("Even",evens)
# print("Double",double)

"""Sum of value"""
# from functools import reduce

# nums = [4,2,9,1,8,6,5]
# def sum_it(a,b):
#   return a+b
# evens = list(filter(lambda n : n%2 == 0,nums))
# double = list(map(lambda n: n*2,evens))
# sum = reduce(sum_it,double)

# print("Even",evens)
# print("Double",double)
# print("Sum",sum)


"""Sum of value using lambda"""
# from functools import reduce

# nums = [4,2,5,1,9,8,6]
# evens = list(filter(lambda n : n%2 == 0,nums))
# double = list(map(lambda n: n*2,evens))
# sum = (reduce(lambda a,b: a+b,double))

# print("Even",evens)
# print("Double",double)
# print("Sum",sum)


"""Sum of cubes of all number in a list"""

# from functools import reduce
# nums = [2,3,4]
# evens = list(filter(lambda n: n%2 == 0,nums))
# cubes = list(map(lambda n: n**3,evens))
# sum = reduce(lambda a,b: a+b,cubes)

# print("Even",evens)
# print("Cube",cubes)
# print("Sum",sum)


"""Example"""
# from functools import reduce
# nums = [2,3,4,5,6,7]
# evens = list(filter(lambda n: n%2 == 0,nums))
# cubes = list(map(lambda n: n*2,evens))
# sum = reduce(lambda a,b:a+b, cubes)
# print("Even:",evens)
# print("Cube:",cubes)
# print("Sum:",sum)



"""Example"""
from functools import reduce
n = [1,2,3,4,5,6,7,8,9,0]
Square = list(map(lambda n: n**2,n))
cubes = list(filter(lambda n: n%2 == 0,Square))
sum = reduce(lambda a,b: a+b,cubes)
print("Square",Square)
print("Cube",cubes)
print("Sum",sum)


