# single line string
print("Let's print single line string.")

# string is enclosed in double quotes or single quotes
name = "Haris"
friend = 'Kamran'

# single quotes and double quotes have same result
print(name)
print(friend)

# if you want to use double quotes in string then enclose string in single quotes
apple = '"Apple" is a fruit, and it is red in color.'
print(apple)


# Multi-line string
print("Let's print multi-line string.")

# if you want to use multiple lines in string
# like this

# I am Haris and I am a student.
# I am learning Python.
# I want to become a software engineer.

# then use triple quotes

bio = '''I am Haris and I am a student.
I am learning Python. and
I want to become a software engineer.'''

print(bio)


# Indexing in string
print("Let's learn indexing in string.")

# string is like a list of characters
# you can access each character using index
# index starts from 0

# H a r i s
name = "Haris"

print(name[0])  # H
print(name[1])  # a
print(name[2])  # r
print(name[3])  # i
print(name[4])  # s
# print(name[5])  # IndexError: string index out of range

# by using loop you can access each character of string one by one

print("Let's access each character of string using loop.")

for char in name:
    print(char)