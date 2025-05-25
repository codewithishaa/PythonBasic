#Sort Arrays Using sort() Method of List
import array as arr

# creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
# converting to list 
sortedList = orgnlArray.tolist()
# sorting the list
sortedList.sort()

# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)