#Raising Exceptions

def divide(a, b):
   if b == 0:
      raise ValueError("Cannot divide by zero")
   return a / b

try:
   result = divide(10, 0)
except ValueError as e:
   print(e)

#custom exception
class MyCustomError(Exception):
   pass

def risky_function():
   raise MyCustomError("Something went wrong in risky_function")

try:
   risky_function()
except MyCustomError as e:
   print(e)


#
def process_file(filename):
   try:
      with open(filename, "r") as file:
         data = file.read()
         # Process data
   except FileNotFoundError as e:
      print(f"File not found: {filename}")
    	# Re-raise the exception
      raise  

try:
   process_file("nonexistentfile.txt")
except FileNotFoundError as e:
   print("Handling the exception at a higher level")