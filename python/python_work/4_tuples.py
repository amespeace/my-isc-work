# Exercise 1. Create tuples

t = (1,) #need , for 1 value
print t[-1]
hundredrange = range(100, 200)
t_1 = tuple(hundredrange) #creates a tuple
print t_1[0]
print t_1[-1]

# Exercise 2. Use the enumerate function
mylist = [23, "hi", 2.4e10]
for (count, item) in enumerate(mylist):
    print count, item

# Exercise 3. Unpacking a list
first, middle, last = mylist
print first
print middle
print last
first, middle, last = last, middle, first #swaps around
print first
print middle
print last



