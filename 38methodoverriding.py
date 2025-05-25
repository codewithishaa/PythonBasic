#Method Overloading in Python
#Method overloading is a feature of object-oriented programming where a class can have multiple methods with the same name but different parameters. To overload method, we must change the number of parameters or the type of parameters, or both.
class example:
   def add(self, a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))


