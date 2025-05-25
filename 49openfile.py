#Opening a File in Write Mode
#This mode is used when you want to write data to a file, starting from scratch each time the file is opened −


file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
print ("File opened successfully!!")


#Opening a File in Append Mode
#This mode is used when you want to add data to the end of the file without altering its existing contents −
file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")

#Writing to a File Using write() Method
#The write() method is used to write a single string to a file. This makes it suitable for various text-based file operations.
# Open a file in write mode
with open("example.txt", "w") as file:
   file.write("Hello, World!\n")
   file.write("This is a new line.\n")
print ("File opened successfully!!")



#Writing to a File Using writelines() Method
#The writelines() method is used to write a list of strings to a file.
# List of lines to write to the file
lines = ["First line\n", "Second line\n", "Third line\n"]

# Open a file in write mode
with open("example.txt", "w") as file:
    file.writelines(lines)

print ("File opened successfully!!")

#Writing to an Existing File
#To add data to an existing file without erasing its contents, you should open the file in append mode ('a').
# Open a file in append mode
fo = open("foo.txt", "a")
text = "I am Isha, I live in Dublin"
fo.write(text)

# Close opened file
fo.close()




