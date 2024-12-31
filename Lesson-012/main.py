# we can find the length of a string using len() function
# syntax: len(string_name)
fruit = "Watermelon"
lenFruit = len(fruit)
print(lenFruit)  # Output: 10


# we can print specific characters from a string using slicing
# syntax: string_name[start:stop]

# end index is not included in the output
# Example-1
name = "Python"
print(name[0:2])  # Output: Py

# Example-2
name = "Python"
print(name[2:5])  # Output: tho

# we can also skip the start or stop index
# if we skip the start index, it will start from the beginning
# Example-3
name = "Python"
print(name[:2])  # Output: Py

# if we skip the stop index, it will go till the end
# Example-4
name = "Python"
print(name[2:])  # Output: thon

# we can also use negative indexing
# Example-5
name = "Python"
print(name[-4:-1])  # Output: tho

# Example-6
name = "Python"
print(name[-4:])  # Output: thon

# Example-7
name = "Python"
print(name[:-4])  # Output: Py