# if & else statements

#Example 1:
age=18
if age>=18:
    print("You can vote!")

#Example 2:
age=16
if age>=18:
    print("You can vote!")
else:
    print("Sorry, you can't vote!")

# The elif statement
score=85
if score>=90:
    print("Grade: A")
elif score>=80:
    print("Grade: B")
elif score>=70:
    print("Grade: C")
else:
    print("Grade: D")

#Multiple if statements
temperature=30
humidity=80
if temperature>25:
    print("It's hot.")
if humidity>70:
    print("It's humid.")

# Nested if/else statements
age=20
has_license=True
if age>=18:
    print("You’re old enough to drive.")
    if has_license:
        print("And you have a license, go ahead!")
    else:
        print("But you need a license first!")
else:
    print("You’re too young to drive.")

#..............................................................#

# Project - Login System

#🔸Variable Declarations
username = "Nagham"
password="12345"

#🔸User Input
input_user=input("Please enter your username: ")
input_password=input("Please enter your password: ")

#🔸Main Condition: Check if username is correct
if input_user==username:

    #🔸Nested Condition: Check if password is correct
    if input_password==password:
        print("Login successful!")
    else:
        print("Wrong password.")

#🔸Else Block: Username is incorrect
else:
    print("User not found.")

#................................................................#

# Challenge - BMI Calculator

# Ask the user to enter weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI and round the result to 2 decimal places
bmi = round(weight / (height ** 2),2)

# Determine the weight category
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are extremely obese.")

#................................................................#

#Homework
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

