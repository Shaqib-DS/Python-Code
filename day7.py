                # lambda functions in python

add = lambda a, b: a + b
print(add(5, 3))

square = lambda x: x * x
print(square(4))  

subtract = lambda a, b: a - b
print(subtract(5, 3))  

divide = lambda a, b: a / b if b != 0 else "Division by zero error"
print(divide(10, 2))
print(divide(10, 0))