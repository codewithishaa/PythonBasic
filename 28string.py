string1='Isha Borgaonkar'
print(string1)
string2="Isha Borgaonkar"
print(string2)
string3='''Isha Borgaonkar'''
print(string3)
string4= """Isha Borgaonkar"""
print(string4)

#Python String Indexing

var = "HELLO PYTHON"
print(var[0]) 
print(var[7])  
print(var[11])  
print(var[12]) 

#Python String Negative & Positive Indexing
var = "HELLO PYTHON"
print(var[-1]) 
print(var[-5])  
print(var[-12]) 
var="HELLO PYTHON"
var[7]="y"
print (var)


#Python String Slicing
var="HELLO PYTHON"

print ("var:",var)
print ("var[3:8]:", var[3:8])


#Python String Slicing With Negative Indexing
var="HELLO PYTHON"
print ("var:",var)
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])

#Default Values of Indexes with String Slicing
var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])\


var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])

var="HELLO PYTHON"
print ("var:",var)
print ("var[0:12]:", var[0:12])
print ("var[:]:", var[:])


#Return Type of String Slicing
var="HELLO PYTHON"

print ("var:",var)
print ("var[:6][:2]:", var[:6][:2])

var1=var[:6]
print ("slice:", var1)
print ("var1[:2]:", var1[:2])
