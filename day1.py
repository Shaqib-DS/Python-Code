#  introduction to Python programming

print("hello world")
print("welcome to python programming")

# python fundamentals

# 1. Variables and Data Types

        #  variables
name = "shaqib"
age = 20
height = 5.8
is_student = True

       # print variables
print(name)
print(age)
print(height)
print(is_student)

        #  check data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

       #  rules of variable
my_name = "shaqib"
name123 = "shaqib"
_name = "shaqib"
    
 # 2. typecasting

a = 20
b = "30"

print(a)
print(type(a))

print(b)
print(type(b))

         # convert b to an integer
c = int(b)
print(c)
print(type(c))

         # convert a into string
d = str(a)
print(d)
print(type(d))

# 3. taking user input

a = input("enter a number")
print(a)
print(type(a))

a = input("enter  first number")
a = int(a)
b = input("enter second number")
b = int(b)
print(a+b)

a = int(input("enter  first number"))
b = int(input("enter second number"))
print(a+b)

# 4.comments,escape sequences & print statements

            #comments
# this is a single line comment

'''
this is a multi-line comment
'''
        
        #  escape sequences
print("hello\nworld") # \n is used for new line
print("hello\tworld") # \t is used for tab space
print("hello\\world") # \\ is used for backslash
print("hello\"world") # \" is used for double quote
print("hello\'world") # \' is used for single quote

        #  print statements
# basic
print("hello")

# multiple items (auto space)
print("hello","world")

# separator change
print("hello","world",sep="-")
print("hello","world",sep="")

# end
print("hello","world", end="...")
print("loading")

# 5. operators

           # Arithmetic Operators
a = 10
b = 3

print(a + b)   #(Addition)
print(a - b)   #(Subtraction)
print(a * b)   #(Multiplication)
print(a / b)   #(Float division)
print(a // b)  #(Integer division - floor)
print(a % b)   #(Modulus - remainder)
print(a ** b)  #(Exponent - 10^3)

         # Comparison Operators
a = 10
b = 10

print(a == b)  #(Equal to)
print(a != b)  #(Not equal to)
print(a > b)   #(Greater than)
print(a < b)   #(Less than)
print(a >= b)  #(Greater than or equal to)
print(a <= b)  #(Less than or equal to)

            # logical operators
a = True
b = False

print(a and b) #both true so true
print(a or b) #one true so true
print(not a) #not a is false

#example with condition

age = 20
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")

        #assignment operators
x = 10
print(x)

x += 5
print(x)

x -= 3
x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x %= 2
print(x)