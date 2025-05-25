# Open the file in read mode
file = open('example.txt', 'r')

# Read the entire content of the file
content = file.read()

# Print the content
print(content)

# Close the file
file.close()


# Open the file in read mode
file = open('example.txt', 'r')

# Read all lines from the file
lines = file.readlines()

# Print the lines
for line in lines:
   print(line, end='')

# Close the file
file.close()


#Reading a File in Binary Mode
#Open the file in binary write mode
with open('test.bin', 'wb') as f:
   data = b"Hello World"
   f.write(data)


