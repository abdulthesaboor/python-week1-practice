# Problem 1: Create a variable for age and print it
age = 23
print("age is:", age)


# Problem 2: Add two numbers using literals and variables, then print the results
print(3 + 5)
num_1 = 3
num_2 = 5
print(num_1 + num_2)


# Problem 3: Take user input for name and print greeting with newline
name = input("Enter you name")
print("Assalam o alaikum! ", name, ", I hope you are doing well.\n Happy Ramadan", sep="")


# Problem 4: Convert string "25" to integer
value_1 = "25"
value_1 = int(value_1)
print(value_1)
print(type(int))


# Problem 5: Calculate simple interest
P = int(input("Please provide the Principal Amount: "))
R = int(input("Please provide the Rate of interest (%)"))
T = int(input("Please provide the Time(Years)"))

SI = (P * R * T) / 100
print(SI)


# Problem 6: Convert temperature (Celsius to Fahrenheit)

# Celsius to Fahrenheit
celsius = float(input("Provide the temprature in Celsius: "))
fahrenheit = (celsius * 1.8 + 32)
print("So the Temprature is", fahrenheit, "fahrenheit")

# Fahrenheit to Celsius
fahrenheit = float(input("provide the temprature in Fahrenheit: "))
celsius = ((fahrenheit - 32) * 5 / 9)
print("So the Temprature is", celsius, "celsius")


# Problem 8: Find type of variable using type()
name = input("Please Enter you Name: ")
age = int(input("Please Enter you Age: "))
degree = input("Please Enter the name of your Degree: ")
print(type(name))
print(type(age))
print(type(degree))


# Problem 9: Create boolean variable and print it
Relegion = bool(input("you are Musllim: True/False: "))
print(type(Relegion))


# Problem 10: Take two numbers as input and print sum
number_1 = int(input("Please type number 1: "))
number_2 = int(input("Please type number 2: "))

print("Sum of the number 1 and number 2: ", number_1 + number_2)
print("Difference of the number 1 and number 2: ", number_1 - number_2)
print("Multiplication of the number 1 and number 2: ", number_1 * number_2)
print("Division of the number 1 and number 2: ", number_1 / number_2)
