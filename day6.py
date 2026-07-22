                    # functions arguments and return values

#positional arguments

def add(a, b):
    return a + b

print(add(5, 3))  

#keyword arguments

def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")

#default arguments

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  
