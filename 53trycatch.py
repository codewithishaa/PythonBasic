try:
   number = int(input("Enter a number: "))
   result = 10 / number
   print(f"Result: {result}")
except ZeroDivisionError as e:
   print("Error: Cannot divide by zero.")
except ValueError as e:
   print("Error: Invalid input. Please enter a valid number.")


try:
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    result = dividend / divisor
    print(f"Result of division: {result}")
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input. Please enter valid integers.")


try:
   file = open("example.txt", "r")
   content = file.read()
   print(content)
except FileNotFoundError:
   print("Error: The file was not found.")
else:
   print("File read operation successful.")
finally:
   if 'file' in locals():
      file.close()
   print("File operation is complete.")

