"""
This program asks the user for two numbers (one is an integer
and the other is a float) and calculates the average of them.
"""

print("This program will ask you for two numbers and calculate the average of them.")

# user input saved in the variables, num_1 and num_2
num_1 = int(input("Enter integer (number without decimal point): "))
num_2 = float(input("Enter floating point number (can have a decimal point): "))

# the average of two numbers is the sum of them divided by 2
average_num = (num_1 + num_2)/2

# printing the average of the numbers
print("The average of " + str(num_1) + " and " + str(num_2) + " is " + str(average_num) + ".")
