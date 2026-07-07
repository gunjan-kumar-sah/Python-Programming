# import sys
# from time import sleep

# sys.setrecursionlimit(300)
# print(sys.getrecursionlimit())

# count = 1

# def greet():
#     global count
#     print("Hello, Gunjan!", count) 
#     count = count + 1
#     sleep(0.02)
#     greet()


# greet()   


# print 1 to 10 number recorsively
from time import sleep
count = 1
def recorsion_num():
     global count
     if count <= 10:
          print(count)
          count += 1
          sleep(0.2)
          recorsion_num()
recorsion_num()