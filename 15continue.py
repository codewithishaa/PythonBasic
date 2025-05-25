
#continue Statement with for Loop
for letter in 'Python':
   if letter == 'h':
      continue
   print ('Current Letter :', letter)
print ("Good bye!")

#continue Statement with while Loop
num = 60
print ("Prime factors for: ", num)
d=2
while num > 1:
   if num%d==0:
      print (d)
      num=num/d
      continue
   d=d+1
   