import sqlite3
import uuid

conn = sqlite3.connect("db.db")

cur = conn.cursor()

print("*"*100)
print("Welcome to the best application in the world which is written by Python")
print("*"*100)

username = input("Please enter your username:")
password = input("Please enter your password:")
email = input("Please enter your email:")
phone = input("Please enter your phone number:")
random_uuid = uuid.uuid4()

query = "INSERT INTO users(id, user, pass, email, phone) VALUES (?, ?, ?, ?, ?)"
values = (str(random_uuid), username, password, email, phone)
cur.execute(query, values)

conn.commit()


