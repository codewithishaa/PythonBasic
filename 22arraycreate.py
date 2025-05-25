#Accessing array items in Python
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

#indexing
print (numericArray[0])
print (numericArray[1])
print (numericArray[2])

#Using iteration
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# iteration through for loop
for item in numericArray:
   print(item)

#Using enumerate() function
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# use of enumerate() function
for loc, val in enumerate(numericArray):
    print(f"Index: {loc}, value: {val}")

