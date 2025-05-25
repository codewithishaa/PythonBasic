# Open a file
fo = open("foo.txt", "wb")
print ("Name of the file: ", fo.name)
print ("Closed or not: ", fo.closed)
print ("Opening mode: ", fo.mode)
fo.close()

with open("example.txt", "r") as file:
   line = file.readline()
   while line:
      print(line, end='')
      line = file.readline()