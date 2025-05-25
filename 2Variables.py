number1 = 10    #Creates an integer variable
number2 = 20    #Creates an integer variable 
name = "Isha"   #Creates a string variable
marks = 95.20   #Creates a floating point variable

#Printing the variables
print (number1)
print (number2)
print (name)
print (marks)

#Deleting the variables in python
counter = 100
print (counter)

#del counter
#print (counter)

#Printing the Types of Variables
x = "Isha"
y =  100
z =  13.10

print(type(x))
print(type(y))
print(type(z))


#Type Casting in python
#Changing the type of variable in python
x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )

#Declaring the multiple variables
a,b,c = 10,20,30
print (a,b,c)


#invalid way of variable declation
"""1num = 100
$_num2  = 100
house-no = 100000

print (1counter)
print ($count)
print (zara-salary)"""

#Local Variables in python
#Python Local Variables are defined inside a function. We can not access variable outside the function.
def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))


#Global variables in python
#Any variable created outside a function can be accessed within any function
x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())