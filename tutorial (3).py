#Variable
name= "Peter"
age= 25

#Type Checking
print(type(name))

#Type Conversion
age_as_text= str(age)

#Check the type
print(type(age_as_text))

# input
major= input("What is your major? ")

#print
print(major)

# 3 Ways to Print Mixed Data Types
print("Age", age)          # Commas
print("Age " + str(age))   # Concatenation
print(f"Age {age}")        # f-string

# Interactive Program
# It calculates age based on your birth year.
name = input("What's your name? ")
birth_year = input("What year were you born? ")
age = 2025 - int(birth_year)
print("Hello " + name + "! You are " + str(age) + " years old.")
print(f"Hello {name}! You are {age} years old.")

# Practice Challenge
city = input("Enter the city? ")
temperature = input("What is the temperature? ")
print(f"It's {temperature}°C in {city}.")