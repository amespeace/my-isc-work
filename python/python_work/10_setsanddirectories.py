# Exercise 1. Create sets
a = set([0, 1, 2, 3, 4, 5])
b = set([2, 4, 6, 8])
print a.union(b)
print a.intersection(b)

# Exercise 2. Collect up counts using a dictionary.
band = ["mel", "geri", "victoria", "mel", "emma"]
counts = {} #empty dictionary
for member in band:
    if member not in counts:
        counts[member] = 1
    else:
        counts[member] += 1
for member in counts:
    print member, counts[member]

# Exercise 3. Useful characteristics of dictionary
if {}: print 'hi' #testing the truth of empty dictionary
d = {"maggie": "uk", "ronnie": "usa"} #create dictionary
dir(d)
print d.items() #prints all
print d.keys() #prints names
print d.values() #prints countries
print d.get("maggie") #returns a value for the key
d.setdefault("None") #setdefault
print d.get("lennie") #returns none



