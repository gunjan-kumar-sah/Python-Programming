class student:
  schoolName = "MUIT, Lucknow"
  def __init__(self,name,degree):
      # print("This is constructor of student class")
      # print("My name is Gunjan kumar sah")

      self.name = name
      self.degree = degree
      print(self.name)
      print(self.degree)

student1 = student("Gunjan", "B.Tech")   #init method is called automatically when object is created
print(student1.schoolName)
print("Student 1 object is: ", student1)
print("Student 1 name is: ", student1.name)
print("Student 1 course is: ", student1.degree)


student2 = student("Arti", "B.A") 
# student2.schoolName = "AKTU, Lucknow"
# print(student2.schoolName)
print(student2)
print("Student 2 name is: ", student2.name)
print("Student 2 course is: ", student2.degree)
