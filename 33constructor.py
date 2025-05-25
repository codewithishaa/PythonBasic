#constructor is an instance method in a class, that is automatically called whenever a new object of the class is created. The constructor's role is to assign value to instance variables as soon as the object is declared.
#Constructor in Python
#constructor which does not accept any parameter other than self is called as default constructo
class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Isha"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))


#Parameterized Constructor
#If a constructor is defined with multiple parameters along with self is called as parameterized constructor.

class Employee:
   'Common base class for all employees'
   def __init__(self, name, age):
      self.name = name
      self.age = age

e1 = Employee("Isha", 24)
e2 = Employee("Ritul", 25)

print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
print ("Name: {}".format(e2.name))
print ("age: {}".format(e2.age))


#Python Multiple Constructors
class Student:
   def __init__(self, *args):
      if len(args) == 1:
         self.name = args[0]
        
      elif len(args) == 2:
         self.name = args[0]
         self.age = args[1]
        
      elif len(args) == 3:
         self.name = args[0]
         self.age = args[1]
         self.gender = args[2]
            
st1 = Student("Isha")
print("Name:", st1.name)
st2 = Student("Shubham", 25)
print(f"Name: {st2.name} and Age: {st2.age}")
st3 = Student("Manisha", 26, "M")
print(f"Name: {st3.name}, Age: {st3.age} and Gender: {st3.gender}")


#Instance Methods
class Employee:
   def __init__(self, name="Manisha", age=24):
      self.name = name
      self.age = age
   def displayEmployee(self):
      print ("Name : ", self.name, ", age: ", self.age)

e1 = Employee()
e2 = Employee("Manisha", 25)

e1.displayEmployee()
e2.displayEmployee()

