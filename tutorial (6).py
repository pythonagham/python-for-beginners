## Iterative Statements
#1 For loop
# Looping through a string
for letter in "Nagham":
    print(letter)

# Looping through a range
for i in range(6):  #range(stop)
    print(i)

for i in range(1, 6):  #range(start,stop)
    print(i)

for i in range(3, 12, 2):  #range(start,stop,step)
    print(i)

for i in range(10, 3, -2):
    print(i)

# Looping through a tuple
numbers = (10, 20, 30, 40)
for num in numbers:
    print(num)

# Looping through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# Looping through a dictionary
dict = {"fruit": "apple", "quantity": 5, "price": 2}
for key in dict:
    print(key)

for key in dict:
    print(dict[key])

#2 While loop
# Printing numbers
i = 1
while i <= 5:
    print(i)
    i += 1

# Counting Down
count = 5
while count > 0:
    print(count)
    count -= 1  # Decreases count by 1
#................................................................#

## Loop Control Statements
# break
#1 Using break with for
for i in range(1, 6):
    if i == 4:
        break
    print(i)   # prints 1, 2, 3

#2 Using break with while
i = 1
while i < 6:
    if i == 4:
        break
    print(i)   # prints 1, 2, 3
    i += 1

# continue
#1 Using continue with for
for i in range(1, 6):
    if i == 4:
        continue
    print(i)   # prints 1, 2, 3, 5

#2 Using continue with while
i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(i)     # prints 1, 2, 3, 5
#................................................................#


# Project - Number Guessing Game
import random

# Random number between 1 and 20
secret_number = random.randint(1, 20)

print("🎮 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 20. You have 5 attempts.")

for attempt in range(1, 6):  # 5 attempts
    guess = input(f"Attempt {attempt}: Enter your guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("❌ Invalid input! Please enter a number.")
        continue  # skip this attempt

    guess = int(guess)

    if guess == secret_number:
        print("✅ Congratulations! You guessed the correct number 🎉")
        break  # end the loop if guessed correctly
    elif guess < secret_number:
        print("🔼 Too low! Try again.")
    else:
        print("🔽 Too high! Try again.")
else:
    # This else runs only if the loop finishes without a break
    print(f"😢 Game Over! The number was {secret_number}.")
#................................................................#

#Homework
#1. Use a while loop to print numbers from 10 down to 1.
i = 10
while i >= 1:
    print(i)
    i -= 1   # decrease by 1 each time

#2. Use a for loop to print all even numbers between 1 and 20.
for i in range(2, 21, 2):  # start at 2, go up to 20, step by 2
    print(i)

#3. Write a loop that goes through the list and prints each fruit.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
#................................................................#


