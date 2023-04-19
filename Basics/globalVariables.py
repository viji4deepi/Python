x = "Awesome"

def myFunc():
    print("python is "+x)   
    
myFunc()    

print()

#Creating variable inside an function
x = "Awesome"

def myFunc():
    x="Fantasic"
    print("Python is " + x)

myFunc()

print("Python is " + x)

print()

#Id we use global keyword we can make variables scope global

def myFunc():
    global x
    x = "Fantastic"
myFunc()

print("Python is "+x)
print()

#
x = "Awesome"

def myFunc():
    global x
    x = "Fantastic"
myFunc()

print("Python is "+x) #It gives output that keyword global is declared

