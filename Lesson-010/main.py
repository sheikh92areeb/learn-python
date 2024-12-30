# we can take user input using input() function
a = input("Enter a name: ")
print("Hello", a)

# input() function always returns a string
x = input("Enter a First number: ")
y = input("Enter a Second number: ")

print(x + y) # this will concatenate the two strings

# to get the sum of two numbers we need to convert them to int
# we can convert a string to int using int() function
print(int(x) + int(y))