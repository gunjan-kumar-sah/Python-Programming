# with open("practice.txt", "w") as f:
#   f.write("Hii everyone\nWe are learning file I/O\n")
#   f.write("using Java. \nI like programmingin java")


# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# with open("practice.txt", "r") as f:
#     data = f.read()
#     word = "learning"
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")

def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

check_for_word()