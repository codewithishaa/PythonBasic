#Inner Classes
#A class defined inside another class is known as an inner class in Python. Sometimes inner class is also called nested class.
class student:
   def __init__(self):
      self.name = "Ashish"
      self.subs = self.subjects()
      return
   def show(self):
      print ("Name:", self.name)
      self.subs.display()
   class subjects:
      def __init__(self):
         self.sub1 = "Phy"
         self.sub2 = "Che"
         return
      def display(self):
         print ("Subjects:",self.sub1, self.sub2)
         
s1 = student()
s1.show()

#types of inner class 
#Multiple Inner Class
#In multiple inner class, a single outer class contains more than one inner class. Each inner class works independently but it can interact with the members of outer class.
class Organization:
   def __init__(self):
      self.inner1 = self.Department1()
      self.inner2 = self.Department2()
        
   def showName(self):
      print("Organization Name: UCD")

   class Department1:
      def displayDepartment1(self):
         print("In Department 1")
            
   class Department2:
      def displayDepartment2(self):
         print("In Department 2")

# instance of OuterClass
outer = Organization() 
# Calling show method
outer.showName()  
# InnerClass instance 1
inner1 = outer.inner1 
# Calling display method
inner1.displayDepartment1() 
# InnerClass instance 2
inner2 = outer.inner2 
# Calling display method
inner2.displayDepartment2() 

#Multilevel Inner Class
#It refers to an inner class that itself contains another inner class. It creates multiple levels of nested classes.

class Organization:
   def __init__(self):
      self.inner = self.Department()

   def showName(self):
      print("Organization Name: UCD")

   class Department:
      def __init__(self):
         self.innerTeam = self.Team1()

      def displayDep(self):
         print("In Department")

      class Team1:
         def displayTeam(self):
            print("Team 1 of the department")

# instance of outer class                
outer = Organization()  
# call the method of outer class
outer.showName()  

# Inner Class instance
inner = outer.inner  
inner.displayDep()  

# Access Team1 instance
innerTeam = inner.innerTeam  
# Calling display method
innerTeam.displayTeam() 