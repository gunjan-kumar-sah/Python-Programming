# a = [1,2,3,4,6,7,8,9]
# b = []
# for i in a:
#   if i%2 == 0:
#     b.append(i)

# print(b)



# nums = [2,3,4,23,45,46,47,82]
# event = []
# for i in nums:
#     if i%2==0: 
#         event.append(i)
# print(event)


"""
nums = [2,3,4,23,45,46,47,82]

def is_even(n):
  return n%2 == 0

event = list(filter(is_even,nums))

print(event)
"""


# nums = [2,3,4,23,45,46,47,82,10,0]

# is_even = lambda n: n%2 == 0

# event = list(filter(is_even,nums))

# print(event)

"""check even odd using filter and lambda"""
nums = [2,3,4,23,45,46,47,82,10,0]

event = list(filter(lambda n : n % 2 == 0,nums))

print(event)


"""Check the number who greater then 50"""

list1 = [12,34,56,78,90,11,23,45,67,89,100,150,200]
greater = list(filter(lambda x : x>=50,list1))
print(greater)