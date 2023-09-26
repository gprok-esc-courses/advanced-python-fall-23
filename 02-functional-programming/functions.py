
def myfunction(x):
    return x * x


# Reference to a function is also a function
square = myfunction


print(square(2))


# Lamda expressions or Anonymous functions
mylist = [1, 2, 3, 4]

# Find the total in the traditional way
total = 0
for value in mylist:
    total += value
print(total)


some_function = lambda s: print(s)
some_function(mylist)


