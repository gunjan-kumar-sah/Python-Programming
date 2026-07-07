# Create class Student that takes 3 marks and has a method average().

class Student:

  def __init__(self, name, listOfMarks):
      self.name = name
      self.listOfMarks = listOfMarks

  # @staticmethod
  def average(self):
      sum = 0
      for eachValue in self.listOfMarks:
          sum = sum + eachValue

      average = sum/len(self.listOfMarks)
      print("Average marks of student is: ", average)  
      


student1 = Student("Gunjan", [90, 80, 70])
print("Student 1 name is: ", student1.name)
print("Student 1 marks are: ", student1.listOfMarks)
student1.average()