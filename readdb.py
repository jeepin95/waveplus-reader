import sqlite3
import tableprint
import datetime


conn = sqlite3.connect('waveplus.db')
c = conn.cursor()

header = ['Date','Radon','Temperature','CO2','VOC']
print(tableprint.header(header, width=22))

for row in c.execute("SELECT * FROM readings"):
    data = [str(row[0]), row[1], row[2], row[3], row[4]]
    print(tableprint.row(data, width=22))
    #print(data)

