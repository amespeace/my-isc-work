# Exercise 2. Using a for statement
gases = ['He', 'Ne', 'Ar', 'Kr']
count = 0
while count < 4:
    item = gases[count]
    print item, gases.index(item)
    count += 1

# Exercise 3. Try out if, elif, else
name = "Lisa"
if name == "Lisa":
    print name, " plays saxophone"
elif name == "Bart":
    print name, " rides skateboard"
else:
    print name, "live in Springfield"
