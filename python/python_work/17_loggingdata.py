# Exercise 1. Import serial module
import serial, io
import datetime datetime

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE
)

# Exercise 2. Get reading
print ser.read(size=8) #8 is specific to device

# Exercise 3 & 4. Add time and date
print datetime.utcnow().isoformat(), ser.read(size=8)
datastring = ser.read(size=8)
print datetime.utcnow().isoformat(), datastring

# Exercise 5. Add a loop to continuosly log data
while ser.isOpen()
    datastring = ser.read(size=8)
    print datetime.utcnow().isoformat(), datastring

# Exercise 6. Rewrite to use readline
import io

sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser, 1), encoding='ascii', newlne='\r')

while ser.isOpen()
    datastring = sio.readline()
    print datetime.utcnow().isoformat(), datastring

# Exercie 7. Print to file
outfile = '/tmp/serial-temperature.tsv'

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 9600,
)

sio = io.TextIOWrapper(
    io.BufferedRWPair(ser, ser, 1)
    encoding = 'ascii', newline = '\r'
)

with open(outfile, 'a') as f: #appends to existing file
    while ser.isOpen():
        datestring = sio.readline()
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n') #\t tab \nline
        f.flush() #force system to write to disk

"""tail -f monitors file and logs at the same time"""



