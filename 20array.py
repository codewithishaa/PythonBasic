import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)


#accessing array elements
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

#Insertion Operation
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
 print(x)


 #Deletion Operation
 from array import *
array1 = array('i', [10,20,30,40,50])
array1.remove(40)
for x in array1:
   print(x)

#Search Operation
from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))


#Update Operation
from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)