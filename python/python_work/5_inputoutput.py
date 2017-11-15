# Exercise 1. Read contents of CSV and display each line.
print "exercise_1"
with open('weather.csv', 'r') as reader:
    data = reader.read()
print data

# Exercise 2. Reading line by line
print "exercise_2"
with open('weather.csv', 'r') as reader:
    line = reader.readline()
    while line != '':
       line = reader.readline()
       print line
print "It's over"


# Exercise 3. Using a for loop for rainfall values
print "exercise_3"
with open ('weather.csv', 'r') as reader:
    header = reader.readline() #readtopline
    rain = []
    for line in reader.readlines():
        r = line.strip().split(",")[-1] #strip to last column
        r = float(r)
        rain.append(r) #append last column to list
print rain
with open ('rain.txt', 'w') as raindata:
    for r in rain:
       raindata.writelines(str(r) + "\n")


# Exercise 4.Writing and reading binary data
import struct #unpack/pack to bianry
bin_data = struct.pack("bbbb", 123, 12, 45, 34)
with open ('mybinary.dat', 'wb') as bwriter:
    bwriter.write(bin_data) #write to file
with open ('mybinary.dat', 'rb') as breader:
    bin_data2 = breader.read() #open to file
data = struct.unpack("bbbb", bin_data2)
print data 

        


