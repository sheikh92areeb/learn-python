num = int(input("Enter a number: "))

if num < 0:
    print("Negative number")
elif num > 0:
    if num <= 10:
        print("number is between 1 to 10")
    elif num > 10 and num <= 20:
        print("number is between 11 to 20") 
    else:
        print("number is greater than 20")       
else:
    print("Zero")