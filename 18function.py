# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


#passing the argument
def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return
   
greetings("Samay")
greetings("Pratima")
greetings("Steven")


#Default Arguments
# Function definition is here
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )
printinfo( name="miki" )



#Arbitrary or Variable-length Arguments
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )


#Function with Return Value
def add(x,y):
   z=x+y
   return z
a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))


#Global vs. Local variables
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total;

# Now you can call sum function
sum( 10, 20 );
print ("Outside the function global total : ", total) 