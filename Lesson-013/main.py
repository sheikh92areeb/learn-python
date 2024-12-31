# String are immutable
# when we use any of string method it will return a new string

# define a string
str1 = "Python is a programming language"

# use the upper method
upper_str = str1.upper()
print(upper_str)

# print the original string
print("Original String: ", str1)

# use the lower method
lower_str = str1.lower()
print(lower_str)

# use the strip method
str2 = "  Python Language  "
strip_str = str2.strip()
print(strip_str)

# use the rstrip method
str3 = "hello !!!"
rstrip_str = str3.rstrip("!")
print(rstrip_str)

# rstrip only remove the trailing characters
str4 = "!Hello !!!"
rstrip_str = str4.rstrip("!")
print(rstrip_str)

# use the replace method
str1 = "Pythone is a programming language"
replace_str = str1.replace("Python", "Java")
print(replace_str)

# use the split method
split_str = str1.split(" ")
print(split_str)

# use the capitalize method
str5 = "my name is kashif"
cap_str = str5.capitalize()
print(cap_str)

# capitalize method turns all other characters into lower except first
str6 = "my Name Is Kashif"
cap_str1 = str6.capitalize()
print(cap_str1)

# use the center method 
str7 = "Welcome to Our Page"
center_str = str7.center(50)
print(center_str)
print(len(str7))
print(len(center_str))

# we can also specify the fill character
center_str = str7.center(50, "*")
print(center_str)

# use the count method
count_str = str7.count("e")
print(count_str)

# use the endswith method
endswith_str = str7.endswith("Page")
print(endswith_str)

# we can also specify the start and end index
endswith_str = str7.endswith("to", 4, 10)
print(endswith_str)

# use the find method
find_str = str7.find("to")
print(find_str)

# if value is not found it will return -1
find_str = str7.find("hello")
print(find_str)

# use the index method
index_str = str7.index("to")
print(index_str)

# if value is not found it will raise an exception
# index_str = str7.index("hello")
# print(index_str) # ValueError: substring not found

# use the isalnum method
str8 = "Python123"
isalnum_str = str8.isalnum()
print(isalnum_str)

# use the isalpha method
str9 = "Python"
isalpha_str = str9.isalpha()
print(isalpha_str)

# use the islower method
lower_str = str9.islower()
print(lower_str)

# use the isprintable method
str10 = "Python"
isprintable_str = str10.isprintable()
print(isprintable_str)

# if we have any non printable character it will return False
str11 = "Python\n"
isprintable_str = str11.isprintable()
print(isprintable_str)

# use the isspace method
str12 = " "
isspace_str = str12.isspace()
print(isspace_str)

# use the istitle method
str13 = "Python Is A Programming Language"
istitle_str = str13.istitle()
print(istitle_str)

# use the isupper method   
str14 = "PYTHON"
isupper_str = str14.isupper()
print(isupper_str)

# use the startswith method
startswith_str = str13.startswith("Python")
print(startswith_str)

# use the swapcase method
swapcase_str = str13.swapcase()
print(swapcase_str)

# use the title method
str15 = "python is a programming language"
title_str = str15.title()
print(title_str)