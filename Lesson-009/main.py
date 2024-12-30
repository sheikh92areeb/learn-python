# typecasting in python
string = "12"
number = 12

# convert string to integer
# error will raise if string contains any other character
string_to_int = int(string)

# sum of two integers
sum = string_to_int + number

# print sum
print(sum)

# Explicit typecasting in python
a = "10"
b = 20
c = int(a) + b

print(c)

# Implicit typecasting in python
a = 10
b = 20.5
c = a + b

print(c)
print(type(c))