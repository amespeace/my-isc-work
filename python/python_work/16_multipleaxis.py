# Exercise 1. Different axis
import matplotlib.pyplot as plt
fig, ax1 = plt.subplots()
time_decade = [0, 1, 2, 3, 4, 5, 6]
CO2_conc = [250, 265, 272, 260, 300, 320, 389]
ax1.plot(time_decade, CO2_conc, 'b--')
ax1.set_ylabel("[CO2]")
ax2 = ax1.twinx()
temp = [14.1, 15.5, 16.3, 18.1, 17.3, 19.1, 20.2]
ax2.plot(time_decade, temp, 'r-')
ax2.set_ylabel("Temp")
#plt.show()
plt.savefig("CO2temps.pdf")

# Exercise 2. Side by side graphs
plt.subplot(1, 3, 1)
x = range(0, 10, 1)
plt.plot(x)
plt.subplot(1, 3, 2)
y = range(10, 0, -1)
plt.plot(y)
plt.subplot(1, 3, 3)
z = [4] * 10
plt.plot(z)
plt.show()
plt.savefig("multiple.pdf")


