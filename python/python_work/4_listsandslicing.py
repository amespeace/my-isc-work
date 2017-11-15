# Exercise 1. Create a simple list
mylist = range(1,6)
print mylist
second_item = mylist[1]
print second_item
secondtolast_item = mylist[-2]
print secondtolast_item
all_list = mylist[0:5]
secondtofourth = mylist[1:3]
print secondtofourth

# Exercise 2. Create a range
one_to_ten = range(1,11)
one_to_ten[0] = 10 #change value
one_to_ten.append(11) #add to end
one_to_ten.extend([12, 13, 14]) #add list
print one_to_ten

# Exercise 3. Combine lists and loops
forward = [] #create empty lists
backward = []
values = ["a", "b", "c"]
for item in values: #loop over items in values
    forward.append(item)
    backward.insert(0, item)

print forward
print backward
forward_r = sorted(forward, reverse=True) #Reverse list order
print forward_r

# Exercise 4. What to do with a list
countries = ["uk", "usa", "uk", "uae"]
#dir(countries)
#help(countries.count) #Open help directory
print countries.count("uk") #Count number of occurence 


