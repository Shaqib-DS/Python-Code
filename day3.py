            # comments

# This is a single-line comment

'''
This is a
multi-line comment
'''
            # escape sequences

print("Hello\nWorld")

print("Hello\tWorld")

print("Hello\\World")

print("Hello\"World\"")

               # print statement

print("hello","how are you?",sep="-")
print("hello","i am fine",end="*")
print("looking good",end="'")

               # operators

# arithmetic operators

a = 10
b = 5

print(a + b) 
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# conditional operators

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# logical operators
c = True
d = False

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

# assignment operators

a = 5
b = 10

a += 5
print(a)

b -= 5
print(b)

a *= 2
print(a)

b /= 2
print(b)

a //= 2
print(a)

b %= 2
print(b)

a **= 2
print(a)

           # control flow and loops

# if statement

age = int(input("Enter your age"))

if age >= 18:
    print("You are eligible to vote.")
print("Thank you for using the program.")


# if-else statement

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# if-elif-else statement
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote.")


# match case statement

a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You entered one.")
    case 2:
        print("You entered two.")
    case 3:
        print("You entered three.")
    case 4:
        print("You entered four.")
    case 5:
        print("You entered five.")
    case 6:
        print("You entered six.")
    case 7:
        print("You entered seven.")
    case 8:
        print("You entered eight.")
    case 9:
        print("You entered nine.")
    case 10:
        print("You entered ten.")
    case _:
        print("Invalid number.")