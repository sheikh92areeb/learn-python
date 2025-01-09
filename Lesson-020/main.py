a = 4
b = 6

gmean = (a * b) / (a + b)
print(gmean)

# we can create a function for calculating Mean

def calculategmean(a,b):
    mean = (a * b) / (a + b)
    print(mean)
    

a= 9
b= 55 
calculategmean(a,b)

# function with conditions

def isgreater(a , b):
    if a > b:
        print("First Number is Greater")
    else:
        print("Second Number is Greater")    

isgreater(a ,b)     


# we define the function but don't write code
# we can just give (pass)

def islesser(a,b):
    pass