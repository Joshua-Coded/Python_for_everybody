# Ask the user to input 2 values and store them in variable num1 and num2

num1, num2 = input("Enter 2 numbers: ").split() 

# Convert the strings into regular number integer

num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum

sum = num1 + num2

#Substract values and store in differnce

diff = num1 - num2

# multiply the values and store in product

prod = num1 * num2

# divide the values and store in quotient

div = num1 / num2

# use modulus on the values to find the remainder

mod = num1 % num2

# print the result on the screen

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, prod))
print("{} / {} = {}".format(num1, num2, div))
print("{} % {} = {}".format(num1, num2, mod))
