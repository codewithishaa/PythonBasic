#Nestedif statement
num = 36
print ("num = ", num)
if num % 2 == 0:
   if num % 3 == 0:
      print ("Divisible by 3 and 2")
print("....execution ends....")


#Nested if Statement with else Condition
num=8
print ("num = ",num)
if num%2==0:
   if num%3==0:
      print ("Divisible by 3 and 2")
   else:
      print ("divisible by 2 not divisible by 3")
else:
   if num%3==0:
      print ("divisible by 3 not divisible by 2")
   else:
      print ("not Divisible by 2 not divisible by 3")

    