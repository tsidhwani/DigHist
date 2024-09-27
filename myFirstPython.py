print("Hello world!")

print(type('3'))
print(type(3.))
print(type(3))
print(type(True))

#first problem
a = 4
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
if(a > b): 
    print("a is greater than b")
else: 
    print(" a is not greater than b")


#second problem
grub = ["grapes", "apples", "strawberries", "peaches", "cherries"]
for fruit in grub:
    print(fruit)
    if(fruit == "peaches"):
        print("this is my favorite^^")

#third problem

journal = {"tim" : 10, "bob" : 20, "timbob" : 30}
for iteration in journal:
    print(iteration, journal[iteration])

journal["bob"] = 50
print(journal["bob"])

#fourth problem

def multiply_numbers(x, y):
    return x * y

print(multiply_numbers(1, 3))

#fifth problem
import math
print(math.sqrt(64))

#last problem
#don't get this, I see the solution but dont get the "with" part


