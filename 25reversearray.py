#Reverse an Array Using reverse() Method
import array as arr

# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

# converting the array into list
newArray = numericArray.tolist()

# reversing the list
newArray.reverse()

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)