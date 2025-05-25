"""It is used to inherit the properties and behaviours of one class to another.
The class that inherits another class is called a child class and the class 
that gets inherited is called a base class or parent class."""

#Single Inheritance
#parent class
#a child class inherits attributes and methods from only one parent class.
class Parent: 
   def parentMethod(self):
      print ("Calling parent method")

# child class
class Child(Parent): 
   def childMethod(self):
      print ("Calling child method")

# instance of child
c = Child()  
# calling method of child class
c.childMethod() 
# calling method of parent class
c.parentMethod() 


#Multiple Inheritance
#construct a class based on more than one parent classes. The Child class thus inherits the attributes and method from all parents. The child can override methods inherited from any parent.
class division:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def divide(self):
      return self.n/self.d
class modulus:
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def mod_divide(self):
      return self.n%self.d
      
class div_mod(division,modulus):
   def __init__(self, a,b):
      self.n=a
      self.d=b
   def div_and_mod(self):
      divval=division.divide(self)
      modval=modulus.mod_divide(self)
      return (divval, modval)
   
x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())

#Method Resolution Order (MRO)
# parent class
class Universe: 
   def universeMethod(self):
      print ("I am in the Universe")

# child class
class Earth(Universe): 
   def earthMethod(self):
      print ("I am on Earth")
      
# another child class
class India(Earth): 
   def indianMethod(self):
      print ("I am in India")      

# creating instance 
person = India()  
# method calls
person.universeMethod() 
person.earthMethod() 
person.indianMethod() 


#Hierarchical Inheritance
#This type of inheritance contains multiple derived classes that are inherited from a single base class. This is similar to the hierarchy within an organization.
# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp1 = Employee1()  
emp2 = Employee2()
# method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod() 
emp2.employee2Method()  



#Hybrid Inheritance
# parent class
class CEO: 
   def ceoMethod(self):
      print ("I am the CEO")
      
class Manager(CEO): 
   def managerMethod(self):
      print ("I am the Manager")

class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Employee one")
      
class Employee2(Manager, CEO): 
   def employee2Method(self):
      print ("I am Employee two")      

# creating instances 
emp = Employee2()
# method calls
emp.managerMethod() 
emp.ceoMethod()
emp.employee2Method()


#super() function
# parent class
class ParentDemo:
   def __init__(self, msg):
      self.message = msg

   def showMessage(self):
      print(self.message)

# child class
class ChildDemo(ParentDemo):
   def __init__(self, msg):
      # use of super function
      super().__init__(msg)  

# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
obj.showMessage()  

