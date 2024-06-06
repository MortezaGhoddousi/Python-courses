
# importing required libraries
import mysql.connector

# Connecting to Database  
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="python24",
  passwd ="python24",
  database = "python24db"
)
 
print(dataBase)
  
  
mycursor = dataBase.cursor()

# Creating database
# try:
#   mycursor.execute("CREATE DATABASE python24db")  
# except:
#   pass

# Creating Table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
  
# Inserting data into database

# sql = "INSERT INTO python24tb (user, pass, email) VALUES (%s, %s, %s)"
# val = ("Mahtab", "321", "ma@gmail.com")
# mycursor.execute(sql, val)  

# user = 'Iman'
# passw = '987'
# email = 'im@gmail.com'

# sql = f"INSERT INTO python24tb (user, pass, email) VALUES ('{user}', '{passw}', '{email}')"
# mycursor.execute(sql)  

# dataBase.commit()

# print(mycursor.rowcount, "record inserted.")

# Getting data from database

# mycursor.execute("SELECT id, user, pass, email, time FROM python24tb")

# myresult = mycursor.fetchall()

# print(myresult)

# for x in myresult:
#   print(x)
  
# Updating data in database

# passw = '123456789'
# id1 = '1'
# sql = f"UPDATE python24tb SET pass = '{passw}' WHERE id = '{id1}'"

# mycursor.execute(sql)

# dataBase.commit()

# print(mycursor.rowcount, "record(s) affected")

# Deleting data from database

id1 = '3'
sql = f"DELETE FROM python24tb WHERE id = '{id1}'"

mycursor.execute(sql)

dataBase.commit()

print(mycursor.rowcount, "record(s) deleted")  

# Disconnecting from the server
dataBase.close()

