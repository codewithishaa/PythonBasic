#Using append() Method
import array as arr

# creating two arrays
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])

# merging both arrays
for i in range(len(b)):
   a.append(b[i])
print (a)


#Using + operator
import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])
x = a.tolist()
y = b.tolist()
z = x+y
a = arr.array('i', z)
print (a)


#Using extend() Method
import array as arr
a = arr.array('i', [88, 99, 77, 66, 44, 22])
b = arr.array('i', [12, 17, 18, 11, 13, 10])
a.extend(b)
print (a)