            # loops

# for loop

for i in range(5):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

# while loop

i = 1
while i <= 10:
    print(i)
    i += 1

# print even numbers

i = 0
while i <= 10:
    print(i)
    i += 2

             # statements

# break statements

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue statements

for i in range(1, 11):
    if i == 5:
        continue

# pass statements

for i in range(1, 11):
    if i == 5:
        pass
    print(i)

                          # strings

name = "shaqib"
name = 'shaqib'
#name = '''data scientist.'''
print(name)

# indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])

# slicing

name = "shaqib khan"
print(name[0:6])
print(name[0:10])
print(name[0:15])
print(name[2:-1])
print(name[1:-2])

# print(name[0:6:n])   # skip n-1 characters
print(name[0:6:2])
print(name[0:10:3])
print(name[0:15:4])
print(name[2:-1:5])
print(name[1:-2:6])

                    # striungs methods and functions

# changing case

text = "hello world"
print(text.upper())     
print(text.lower())  
print(text.title())  
print(text.capitalize())  

# remove white space

text = "  hello world  "
print(text.strip())  
print(text.lstrip()) 
print(text.rstrip()) 

# finding and replacing

text = "Python is fun"
print(text.find("is"))  
print(text.replace("fun", "awesome"))  

# splitting and joining

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  

new_text = " - ".join(fruits)
print(new_text)  

# checking string properties

text = "Python123"
print(text.isalpha())  
print(text.isdigit())  
print(text.isalnum())    

# get length of string

text = "Hello, Python!"
print(len(text)) 

# character encoding

print(ord('A'))  
print(chr(65))   

name = "shaqib"
age = 20
print("My name is {} and I am {} years old.".format(name, age))

template = "Dear {} you are awesome"
name = "shaqib"
print(template.format(name))