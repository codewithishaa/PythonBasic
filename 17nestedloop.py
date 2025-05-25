#Python Nested for Loop
months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]

for x in months:
  for y in days:
    print(x, y)

print("Good bye!")

#python nested while loop
i = 2
while(i < 25):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!")

