#Data type: Used to define the type of a variable
#It represents the type of data we are going to store in a variable and 
#determines what operations can be done on it.

#Numeric Data types in python
#Store numeric values.

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type

#printing the variables
print(var1)
print(var2)
print(var3)
print(var4)


#String Data Types
#Sequence of one or more characters, enclosed in single, double or triple quotes
str = 'Ireland'
str2="Isha"
str3='''Dublin'''


print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "Country") # Prints concatenated string

#Python Sequence Data types
#list data type 
#list can be of different data type
#list contains items separated by commas and enclosed within square brackets ([])
list = [ 'Isha', 786 , 2.23, 'ucd', 70.2 ]
tinylist = [123, 'ucd']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

#Python Tuple Data Type
#sequence data type that is similar to a list. 
#values separated by commas.
#tuples are enclosed within parentheses (...).

tuple = ( 'isha', 786 , 2.23, 'manisha', 70.2  )
tinytuple = (123, 'deepak')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples



#Python Bytes Data Type
# Using bytes() function to create bytes
#represents a sequence of bytes. Each byte is an integer value between 0 and 255. store binary data
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  

#Python Bytearray Data Type
# it is mutable, we can modify the values stored in it after it is created.
value = bytearray([72, 101, 108, 108, 111])  
print(value) 

#Python Memoryview Data Type
#view into the memory of the original object
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)


#Python Dictionary Data Type
#consist of key:value pairs.
#Dictionaries are enclosed by curly braces ({ }) 
tinydict = {'name': 'Manisha','code':6734, 'dept': 'sales'}
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


#Python Set Data Type
set1 = {123, 452, 5, 6}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1)
print(set2)


#Python Boolean Data Type
#evaluate the value of any expression and returns either True or False based on the expression.
a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))

#Python None Type
#none type is represented by the "nonetype." 
x = None

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))



#data type Conversion
print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3.3")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)