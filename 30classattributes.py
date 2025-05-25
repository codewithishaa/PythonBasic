#Accessing Class Attributes
#The object name followed by dot notation (.) is used to access class attributes.
class Employee:
   name = "Shubham Aggarwal"
   age = "30"

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)


#Modifying Class Attribute
class Employee:
   # class attribute    
   empCount = 0
   def __init__(self, name, age):
      self.__name = name
      self.__age = age
      # modifying class attribute
      Employee.empCount += 1
      print ("Name:", self.__name, ", Age: ", self.__age)
      # accessing class attribute
      print ("Employee Count:", Employee.empCount)

e1 = Employee("Shreyas", 24)
print()
e2 = Employee("Avadhut", 26)