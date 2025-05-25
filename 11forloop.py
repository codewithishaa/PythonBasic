#Python for Loop with Tuples
#printing addition of numbers in tuple
numbers = (34,54,67,21,78,97,45,44,80,19)
total = 0
for num in numbers:
   total += num
print ("Total =", total)


#range(start, stop, step)
#Start − Starting value of the range. Optional. Default is 0
#Stop − The range goes upto stop-1
#Step − Integers in the range increment by the step value. Option, default is 1.
for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')

#For Loop with Dictionaries
numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
for x in numbers:
   print (x,":",numbers[x])

#For loop to iterate between 10 to 20
for num in range(10, 20):  
   #For loop to iterate on the factors 
   for i in range(2,num): 
      #If statement to determine the first factor
      if num%i == 0:      
         #To calculate the second factor
         j=num/i          
         print ("%d equals %d * %d" % (num,i,j))
         #To move to the next number
         break 
      else:                  
         print (num, "is a prime number")
         break
