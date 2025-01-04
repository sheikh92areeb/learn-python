# Break Statements
# we can use break statement to stop the loop before it has looped through all the items in the list

# Example
for i in range(12):
    if i == 10:
        break
    print("4 x", i + 1, "=", 4 * (i + 1))
print("End of the loop is on the 10th iteration")

# Explanation
# The loop will stop when the value of i is 10
# Last two iterations will not be executed

# Continue Statements
# we can use continue statement to skip the current iteration and continue with the next iteration

# Example
for i in range(1, 12):
    if i == 10:
        print("Skip the iteration")
        continue
    print("4 x", i, "=", 4 * i)

#Explanation
# The loop will skip the iteration when the value of i is 10
# The loop will continue with the next iteration