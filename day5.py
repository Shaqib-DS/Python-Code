              # functions and modulus

# function 

a = 4
b = 2
c = 6

average = (a + b + c) / 3
print(average)
print("The average of", a, b, c, "is", average)

def average(a,b,c):
    d = (a + b + c) / 3
    print(d)

average(4, 2, 6)
     

def average(a,b,c):
    d = (a + b + c) / 3
    return(d)

x = average(4, 2, 6)

print("The average of", a, b, c, "is", x)
print(x)

     
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  