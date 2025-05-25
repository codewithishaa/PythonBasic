#Static Method
"""static method is a type of method that does not require any instance to be called. 
It is very similar to the class method but the difference is that the static method 
doesn't have a mandatory argument like reference to the object − self or reference to 
the class − cls."""
class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   
   # creating staticmethod
   def showcount():
      print (Employee.empCount)
      return
   counter = staticmethod(showcount)

e1 = Employee("Isha", 24)
e2 = Employee("Shubham", 26)
e3 = Employee("Ritul", 27)

e1.counter()
Employee.counter()


#Using staticmethod() Function
class Student:
   stdCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Student.stdCount += 1
   
   # creating staticmethod
   @staticmethod
   def showcount():
      print (Student.stdCount)

e1 = Student("Bhavana", 24)
e2 = Student("Rajesh", 26)
e3 = Student("John", 27)

print("Number of Students:")
Student.showcount()