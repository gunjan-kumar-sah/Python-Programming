# dict = {
#   "name" : "Gunjan",
#   "cgpa" : "8.7",
#   "marks" : [87,85,45],
# }
# print(dict)


student = {
  "name" : "Gunjan",
  "score" : {
    "chem": 57,
    "math": 89,
    "phy": 68
  }
}

student1 = {
  "name" : "Rahul",
  "score" : {
    "chem": 78,
    "math": 56,
    "phy": 98
  }
}
print(student)
# print(student["score"]["math"])
student.keys()
print(student)

student.values()
print(student)

student.items()
print(student)

student.get("score")
print(student)

student.update(student1)
print(student)