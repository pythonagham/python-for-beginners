a=10
b=3
#1 Arithmetic Operators
#Addition
print(a+b)

#Subtraction
print(a-b)

#Multiplication
print(a*b)

#Division
print(a/b)

#Floor Division
print(a//b)

#Modulo
print(a%b)

#Exponentiation
print(a**b)
#...........................................................#

#2 Assignment Operators
#Assignment
x=5

#Addition Assignment
x+=3      #same as x=x+3
print(x)

#Multiplication Assignment
x*=2      #same as x=x*2

#Subtraction Assignment
x-=4      #same as x=x-4

#Division Assignment
x/=3      #same as x=x/3

#Exponentiation Assignment
x**=2
print(x)

#Modulus Assignment
x%=3
print(x)
#...........................................................#

a=10
b=20
#3 Comparison Operators
#Equal to
print(a==b)

#Not equal to
print(a!=b)

#Greater than
print(a>b)

#Less than
print(a<b)

#Greater than or equal to
print(a>=10)

#Less than or equal to
print(b<=15)
#...........................................................#

#4 Logical Operators
#AND
print(a>5 and b<10)

#OR
print(a<10 or b<25)

#NOT
print(not(a==b))
#...........................................................#

#5 Expression
result = a + b *2
print(result)

result = (a + b) *2
print(result)

#6 Operator Precedence (PEMDAS)
total = ((7+3)*2**3)/(10-2)+5%3-1

# P: 7+3=10, 10-2=8
# E: 2**3=8
# MD: 10*8=80, 80/8=10, 5%3=2
# AS: 10+2-1=11
print(total)
#...........................................................#

#7 Mini Project
print("Simple Calculator")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Select operation:")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exponentiation")

choice = input("Enter choice (1/2/3/4/5): ")

if choice == "1":
    print(f"Result: {a + b}")
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero.")
elif choice == "5":
    print("Result:", a ** b)
else:
    print("Invalid choice")
