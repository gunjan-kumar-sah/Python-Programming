f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)
# print(type(data))

line2 = f.readline()
print(line2)


line3 = f.readline()
print(line3)

f.close()

