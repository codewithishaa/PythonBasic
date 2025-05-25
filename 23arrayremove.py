import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.remove(311)
# after removing array
print ("After removing:", numericArray)


#Remove Items from Specific Indices
import array as arr

# creating array
numericArray = arr.array('i', [111, 211, 311, 411, 511])

# before removing array
print ("Before removing:", numericArray)
# removing array
numericArray.pop(3)
# after removing array
print ("After removing:", numericArray)