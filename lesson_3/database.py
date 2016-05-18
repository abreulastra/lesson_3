# -*- coding: utf-8 -*-
"""
Created on Wed May 18 13:15:48 2016

@author: AbreuLastra_Work
"""

# Import sqlite3 and panda, to work with databases and dataframes
import sqlite3 as lite
import pandas as pd

# Connect to the database
con = lite.connect('getting_started.db')

# Creating tuples to add data to our tables
cities = (('Boston', 'MA'), ('Decatur','TX'), ('Washington','DC'))
weather = (('Boston', 2014, 'July', 'January', 65), ('Decatur', 2014, 'July', 'December', 100), ('Washington', 2014, 'May', 'February', 90))


# Update tables
with con:
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS cities')
    cur.execute('DROP TABLE IF EXISTS weather')
    cur.execute('CREATE TABLE cities (name text, state text)')
    cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer)')
    cur.executemany('INSERT INTO cities VALUES(?,?)', cities)
    cur.executemany('INSERT INTO weather VALUES(?,?,?,?,?)', weather)

    # Join data together and find city when July is the warmest month
    cur.execute("SELECT name, state FROM cities INNER JOIN weather ON name = city WHERE warm_month = 'July'")
    
    # Load it 
    rows = cur.fetchall()
    cols =[desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)
    
    # Print out resulting cities
    
    print ("The cities that are the warmest in July are:")
    for index, row in df.iterrows():
        print row['name'], row['state']
    