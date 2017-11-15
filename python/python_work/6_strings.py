# Exercise 1. Loop through a string
s = "I love to write python"
for i in s:
    print i
print s[4]
print s[-1]
print len(s)
print s[0], s[0][0], s[0][0][0]

# Exercise 2. Splitting a string to link through own words
split_s = s.split()
for word in split_s:
    if word.find('i') > -1:
        print "I found 'i' in: '{0}'".format(word)

# Exercise 3. Useful aspects of strings
something = "Completely Different"
print dir(something)
print something.count("t")
print something.find("plete")
split_e = something.split('e')
thing2 = something.replace("Different", "Silly")
print thing2



