class Employee:
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      Employee.empCount += 1
   def showcount(self):
      print (self.empCount)
      
   counter = classmethod(showcount)

e1 = Employee("Isha", 24)
e2 = Employee("Shubham", 26)
e3 = Employee("Ritul", 27)

e1.showcount()
Employee.counter()