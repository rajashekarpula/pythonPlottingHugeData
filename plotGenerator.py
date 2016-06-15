#!/usr/bin/python

import sqlite3 as sql
import matplotlib.pyplot as plt

tcp = []
udp = []
connection = sql.connect('pythonDatabase.sqlite')
c = connection.cursor()

c.execute("SELECT TYPE,SIZE,rowid FROM pythonTable")
rows = c.fetchall()
for row in rows:
    if row[0] == 'TCP':  # If TYPE is TCP then add the value else add 0
        tcp.append(row[1])
        udp.append(0)

    else:                # If TYPE is UDP then add the value else add 0
        udp.append(row[1])
        tcp.append(0)

connection.close()

plt.figure(figsize=(40,40))
plt.xlabel("Number of Rows in the table") # Label for X-axis
plt.ylabel("TCP and UDP Sizes") # Label for Y-axis

plt.plot(tcp,'r+')
plt.plot(udp,'gx')

plt.legend(('TCP','UDP')) # Creates legend based with respect to xAxis and yAxis
#plt.show() # Displays the image generated....// have to zoom to see clearly
plt.savefig('Plot.png') # Creates an image of 40X40