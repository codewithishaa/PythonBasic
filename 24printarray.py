#Python while Loop with Array
import array as arr

# creating array
a = arr.array('i', [96, 26, 56, 76, 46])

# checking the length
l = len(a)

# loop variable
idx = 0

# while loop
while idx < l:
   print (a[idx])
   # incrementing the while loop
   idx+=1


#Loop with Array Index
   import array as arr
a = arr.array('d', [56, 42, 23, 85, 45])
l = len(a)
for x in range(l):
   print (a[x])


#copyarray
import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b = a
print("Copied array:",b)