import sqlite3

conn = sqlite3.Connection('python26db.db')

crsr = conn.cursor()

# # Inserting data into database
# _id = int(input('Enter the id: '))
# username = input('Enter Username: ')
# password = input('Enter Password: ')
# email = input('Enter Email: ')

# query = f"INSERT INTO python26tb (id, username, password, email) VALUES ('{_id}', '{username}', '{password}', '{email}')"

# crsr.execute(query)


# # Getting data from database

# query = f"SELECT * FROM python26tb WHERE id=2"

# data = crsr.execute(query)

# print(list(data))

# # Updating data in database

# query = f"UPDATE python26tb SET password='000' WHERE id=2"

# data = crsr.execute(query)

# Deleting data in database

query = f"DELETE FROM python26tb WHERE id=2"

data = crsr.execute(query)

conn.commit()

conn.close()


