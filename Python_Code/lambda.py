# def fun(num):
#      return num*num
# result = fun(5)
# print(result)


"""def fun(num):
     return num*num

square = fun

result = square(5)
print(result)"""



# lambda function
fun = lambda num: num*num

result = fun(5)
print(result)


add = lambda a,b: a+b   # Lambda Function with two arguments
result = add(4,5)
print(result)


 # chack the grater number
func = lambda a,b,c: a if a>b and a>c else b if b>c else c   # Lambda Function with three arguments
result = func(1,5,3)
print("The num is greater the other number",result)


# To check even odd
evenodd = lambda num : "Even" if num%2 == 0 else "Odd"
result = evenodd(345)
print(result)


# To find the cube of a number 
cube = lambda num: num*num*num
result = cube(3)
print("Cube of a number:-- ",result)




