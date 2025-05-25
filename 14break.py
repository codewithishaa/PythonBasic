#break Statement with for loop
for letter in 'Python':    
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")

#break Statement with while loop
var = 10                   
while var > 0:              
   print ('Current variable value :', var)
   var = var -1
   if var == 5:
      break

print ("Good bye!")

#break Statement with Nested Loops
no = 33
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
   if num == no:
      print ('number found in list')
      break
else:
   print ('number not found in list')

