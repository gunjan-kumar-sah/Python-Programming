from array import *


# This is a array|||


# arr1 = array('i', [12,32,14,111,34])

# # print(arr1)

# # print(arr1.tolist())

# print(arr1.buffer_info())

# for n in arr1:
#   print(n)

"""
arr2 = array('d', [2.5,4.8,-3.2,6.7])

for h in arr2:
  if h < 0:
    continue
  print(h) """

#  this is a list not a array
# arr = [1,2,3,4,5,64,21]
# print(type(arr))


#  This is a typew of array
# arr3 = array("d", [2.0,5.6,3.5,6.1])
# print(type(arr3))

# arr3.append(7.4)
# arr3.append(0.23)
# arr3.remove(7.4)


# for n in arr3:
#   print(n)



"""arr1 = array('i', [10,20,30,40,50])
# # arr2 = array("i",arr1.tolist())
# arr2 = array(arr1.typecode,arr1.tolist())
arr2 = array(arr1.typecode,(n for n in arr1))

arr1[2] = 310

print(arr1)
print(arr2)"""


from array import *
arr = array('i', [10,20,5,23])
# arr.sort()
print(arr)

arr.append(6)
print(arr)
arr.reverse()
print(arr)