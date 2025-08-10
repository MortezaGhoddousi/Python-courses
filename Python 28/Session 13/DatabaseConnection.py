import sqlite3
import uuid

class DataBaseUsers():
    def __init__(self):
        pass

    def ConnectionDB(self):
        self.conn = sqlite3.connect("db.db")
        self.cur = self.conn.cursor()
        print("Connection to the database successfully!")

    def AddNewData(self, user, password, email, phone):
        random_uuid = uuid.uuid4()
        query = "INSERT INTO users(id, user, pass, email, phone) VALUES (?, ?, ?, ?, ?)"
        values = (str(random_uuid), user, password, email, phone)
        self.cur.execute(query, values)
        self.conn.commit()
        print("Inserting data into the database successfully!")

    def getAllUsers(self):
        query = "SELECT * FROM users"
        self.cur.execute(query)
        users = self.cur.fetchall()
        return users
    
    def getUser(self, user, password):
        query = "SELECT * FROM users WHERE user=? AND pass=?"
        values = (user, password)
        self.cur.execute(query, values)
        user = self.cur.fetchall()
        return user
    
    def UpdateData(self, Type, user, password, newPassword=None, newEmail=None, newPhone=None):
        if Type == "password":
            query = "Update users SET pass=? WHERE user=? AND pass=?"
            values = (newPassword, user, password)
            self.cur.execute(query, values)
            self.conn.commit()
        elif Type == "email":
            query = "Update users SET email=? WHERE user=? AND pass=?"
            values = (newEmail, user, password)
            self.cur.execute(query, values)
            self.conn.commit()
        elif Type == "phone":
            query = "Update users SET phone=? WHERE user=? AND pass=?"
            values = (newPhone, user, password)
            self.cur.execute(query, values)
            self.conn.commit()
        print("Updating data from the database successfully!")

    def DeleteUser(self, user, password):
        query = "DELETE FROM users WHERE user=? AND pass=?"
        values = (user, password)
        self.cur.execute(query, values)
        self.conn.commit()
        print("Deleting data from the database successfully!")




        
