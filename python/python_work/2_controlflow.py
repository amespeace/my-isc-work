# Exercise 1: Create some while loops

# Never ending loop
x = 3 
while x < 2:
    print x
    x = 1

# Loop never gets called
y = 4
while y > 5:
    print y
else:
    print "yellow"

# Exercise 2: Using the for statement

mylist = [23, "hi", 2.4e-10]
count = 0
while count < 3:
    item = mylist[count] #assign to temporary variable
    print item, mylist.index(item) #print each item and position
    count += 1

# Exercise 3: Testing truth with 'if' or 'while'

x = 1
if x:
    print x, " is True"

y = 22.1
if y:
    print y, " is True"

z = 0
if z:
    print z, " is True"

a = []
if a:
    print a, " is True"



