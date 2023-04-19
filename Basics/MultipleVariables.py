# Many Values to Multiple Variables

x,y,z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)
print()
#One value to multiple variables

x=y=z = "Mango"

print(x)
print(y)
print(z)
print()
# Unpack a Collection
fruits = ["PineApple", "Strawberry", "Blackberry"]
x,y,z = fruits

print(x)
print(y)
print(z)
print()


#Multiple values seperated by comma 
x = "Python"
y="is"
z = "Awesome"

print(x,y,z) # Python is Awesome
print(x + y + z) #PythonisAwesome

x = "Python "
y="is "
z = "Awesome"
print(x + y + z) #Python is Awesome


#Single line input and output
x = "Python is Awesome"
print(x)
print()

#numerical operators
x = 10
y = 4
print(x+y) #14
print()


x= 5
y = "Marry"
# print(x+y) gives error int + string

print(x,y) # it does not gives error 

