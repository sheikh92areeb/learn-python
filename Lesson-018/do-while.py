# we can emulate a do-while loop in python using while loop
# we can use break statement to break the loop

while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break