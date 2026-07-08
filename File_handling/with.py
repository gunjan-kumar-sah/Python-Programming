with open("with.txt", "r") as f:
  data = f.read()
  print(data)


with open("with.txt", "w") as f:
  f.write("Gunjan kumar sah")
  # f.close()