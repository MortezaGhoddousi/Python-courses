import sqlite3

# # connection to the database
conn = sqlite3.connect('newdb.db')

cursor = conn.cursor()


# # inserting new data into the database
# username = input('enter your username: ')
# password = input('enter your password: ')
# email = input('enter your email: ')

# cursor.execute(f"INSERT INTO user (id, username, password, email) VALUES ('{2}', '{username}', '{password}', '{email}')")

# conn.commit()

# # getting data from the database
# cursor.execute('SELECT * FROM user')
# rows = cursor.fetchall()
# print(rows)

# # updating data from the database
# newPassword = input('enter your new password: ')
# cursor.execute(f"UPDATE user SET password='{newPassword}' WHERE id=1")
# conn.commit()

# # deleting data from the database

# cursor.execute('DELETE FROM user WHERE id=2')
# conn.commit()

conn.close()