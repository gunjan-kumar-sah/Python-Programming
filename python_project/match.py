# num = int(input("Enter a number"))

# match num:

#  case 1:
#   print("One")
#  case 2:
#   print("Two")
#  case 3:
#   print("Three")
#  case 4:
#   print("Four")
#  case 5:
#   print("Five")
#  case _:
#   print("Incorrect")       


num = 5645
match num % 3:
  case 0:
    print("Divisible by 3")
  case 1:
    print("Remaider 1 when divided by 3")
  case _:
    print("Remainder 2 when divided by 3")