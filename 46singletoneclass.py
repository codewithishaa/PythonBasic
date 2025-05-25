#Singleton class is the implementation of singleton design pattern which means this type of class can have only one object. This helps in optimizing memory usage when you perform some heavy operation, like creating a database connection.
#Using __init__
#initializing a newly created object.
class Singleton:
  __uniqueInstance = None

  @staticmethod
  def createInstance():
    if Singleton.__uniqueInstance == None:
      Singleton()
    return Singleton.__uniqueInstance
    
  def __init__(self):
      if Singleton.__uniqueInstance != None:
          raise Exception("Object exist!")
      else:
          Singleton.__uniqueInstance = self
           
obj1 = Singleton.createInstance()
print(obj1)
obj2 = Singleton.createInstance()
print(obj2)


#Using __new__
class SingletonClass:
   _instance = None
   
   def __new__(cls):
      if cls._instance is None:
         print('Creating the object')
         cls._instance = super(SingletonClass, cls).__new__(cls)
      return cls._instance
      
obj1 = SingletonClass()
print(obj1)

obj2 = SingletonClass()
print(obj2)