#!/usr/bin/python

import mysql.connector
from mysql.connector import Error
#import pandas as pd

#Establish connection with the server
conn = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="ALBARRACIN",
   database="infoDB"
)
print(conn)
print("MySQL Database connection successful")


#Creating a cursor
cursor = conn.cursor()

#Preparing SQL Query

def data_entry(): 
    last_name = input('Input LastName : ')
    first_name = input('Input First Name : ')
    dob = input('Input Day of Birth: ')
    id_number = input('Input ID Number: ')
    sex = input('Input sex: ')
    hair = input('Input Color of hair: ')
    eyes = input('Input Color of eyes: ')
    civil_status = input('Input Civil Status: ')
    qualification = input('Input Qualification: ')
    
    cursor.execute("INSERT INTO main_table(last_name, first_name, dob, id_number, sex, hair, eyes, civil_status, qualification) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (last_name, first_name, dob, id_number, sex, hair, eyes, civil_status, qualification)) 
  
    conn.commit()


data_entry()
