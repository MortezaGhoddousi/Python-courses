import sqlite3 as db
import random

# Connecting to database
conn = db.connect("./db.db")
cursor = conn.cursor()

# # Inserting data into database
# username = input('enter your username: ')
# password = input('enter your password: ')
# email = input('enter your email: ')
# Id = random.randint(0, 200)

# try:
#     query = f"INSERT INTO user (id, username, password, email) VALUES (?, ?, ?, ?)"
#     cursor.execute(query, (Id, username, password, email))
#     print("Inserting data into the database successfully")
# except:
#     print("There are some issues on inserting data! Try again")
# finally:
#     conn.commit()
#     conn.close()

# # Getting data from database 
# try:
#     # query = f"SELECT * from user"
#     query = f"SELECT email, password from user WHERE id=?"

#     result = cursor.execute(query, (36,))
#     print(result.fetchall())
# except:
#     print("There are some issues on inserting data! Try again")
# finally:
#     conn.commit()
#     conn.close()

# # Deleting data from database 
# try:
#     # query = f"SELECT * from user"
#     query = f"DELETE FROM user WHERE id=?"
#     cursor.execute(query, (4,))
# except:
#     print("There are some issues on inserting data! Try again")
# finally:
#     conn.commit()
#     conn.close()

# Updating data from database 
try:
    # query = f"SELECT * from user"
    newPassword = input('enter your new password: ')
    query = f"UPDATE user SET password=? WHERE id=?"
    cursor.execute(query, (newPassword, 176))
except:
    print("There are some issues on inserting data! Try again")
finally:
    conn.commit()
    conn.close()


