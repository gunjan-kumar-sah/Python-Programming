# def check_for_word():
#     word = "xlearning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("Found")
#         else:
#             print("Not Found")


# Check a word whose in this line 

def check_for_line():
    word = "xlearning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1        
print(check_for_line())