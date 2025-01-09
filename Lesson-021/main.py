# We can pass Default Argument

def hello_world(fname = "Sameer", lname = "Khan"):
    print("Hello! " + fname + " " + lname)

hello_world("Areeb", "Sheikh")    

# We can pass Required Arguments

def greeting(greeting , name):
    print(greeting + " " + name)

greeting("hello", "Ali")    

# We can pass Keyword Arguments

hello_world(lname="Khan", fname="Farhan")

# We can pass Variable-length Arguments
# 1st Arbitrary variable Arguments

def avarage(*numbers):
    for i in numbers:
        sum = 0
        sum = sum + i
    print("The Avarege is", sum / len(numbers) )

avarage(2,4,5,33,7,2,5)        

# 2nd Keyword Arbitrary Arguments

def name(**names):
    print("Hello! ", names["fname"] , names["lname"])

name(fname="Ali", lname="Khan")    


# We can pass Return statement to get the value

def add(a,b):
    return a + b

c = add(2,5)
print(c)