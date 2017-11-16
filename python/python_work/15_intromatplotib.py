# Exercise 1. Creating a plot
import matplotlib.pyplot as plt
"""plt.plot(range(10))
#plt.show()"""

# Exercise 2 & 3. Plot of chemistry data
time_decade = [0, 1, 2, 3, 4, 5, 6]
CO2_conc = [250, 265, 272, 260, 300, 320, 389]
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
plt.plot(time_decade, CO2_conc, 'g--', temp, 'r-')
plt.title("CO2 concentration over decades")
plt.xlabel("Decade")
plt.ylabel("[CO2]")
plt.show()

plt.savefig("chemistrydata.pdf")
