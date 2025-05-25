#Interfaces
#an interface is a software architectural pattern. It is similar to a class but its methods just have prototype signature definition without any executable code or implementation body. 
#Formal Interface
#Formal interfaces in Python are implemented using abstract base class (ABC). To use this class, you need to import it from the abc module.
from abc import ABC, abstractmethod

# creating interface
class demoInterface(ABC):
   @abstractmethod
   def method1(self):
      print ("Abstract method1")
      return

   @abstractmethod
   def method2(self):
      print ("Abstract method1")
      return
   
   # class implementing the above interface
class concreteclass(demoInterface):
   def method1(self):
      print ("This is method1")
      return
   
   def method2(self):
      print ("This is method2")
      return

# creating instance      
obj = concreteclass()

# method call
obj.method1()
obj.method2()


#Informal Interface
class demoInterface:
   def displayMsg(self):
      pass

class newClass(demoInterface):
   def displayMsg(self):
      print ("This is my message")
  
# creating instance      
obj = newClass()

# method call
obj.displayMsg()