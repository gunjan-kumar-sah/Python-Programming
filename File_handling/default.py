# f = open("sample.txt", "w")

# f = open("gunjan.txt", "a")

# f.close()


"""
f = open("demo.txt", "r+")
f.write("Arti")

print(f.read())
f.close()
"""
# f = open("demo.txt", "w+")
# print(f.read())
# f.write("My name is Gunjan")
# f.close()


f = open("demo.txt", "a+")
print(f.read())
f.write("\nabcdefghijklmnopqrstuvwxyz")
f.close()