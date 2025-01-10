tup = (1,3,4,6,7)

print(tup)
print(type(tup))


# if we make tuple only one item 
# we have to put (,) at end

tup1 = (1,)


# we call tuple items by indexes as same as list

print(tup[0])
print(tup[1])
print(tup[-1])

# with conditions

if 5 in tup:
    print("Is present")
else:
    print("is Absent")    