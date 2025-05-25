#Adding Elements to Python Array
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)


#Using insert() method
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)