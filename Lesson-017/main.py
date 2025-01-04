# Loop on string
name = "Abdul Hadi"
for i in name:
    print(i)


# we can do anything in the loop
name = "Abdul Hadi"
for i in name:
    print(i)
    if i == "d":
        print("Found d")
    

# Loop on list
fruits = ["Apple", "Banana", "Cherry", "Dates"]
for fruit in fruits:
    print(fruit)


# we can also use loop in loop
fruits = ["Apple", "Banana", "Cherry", "Dates"]
for fruit in fruits:
    print("Fruit: ", fruit)
    for i in fruit:
        print(i)


# we can define range in loop by using range() function
for i in range(10):
    print(i)


# we can also define range with start and end
for i in range(1, 10):
    print(i)


# we can also define range with start, end and step
for i in range(1, 10, 2):
    print(i)