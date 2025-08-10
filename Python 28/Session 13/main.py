from DatabaseConnection import DataBaseUsers

db = DataBaseUsers()
db.ConnectionDB()

print("*"*100)
print("Welcome to the best application in the world which is written by Python")
print("*"*100)

# username = input("Please enter your username:")
# password = input("Please enter your password:")
# email = input("Please enter your email:")
# phone = input("Please enter your phone number:")

# db.AddNewData(username, password, email, phone)
users = db.getAllUsers()
user = db.getUser("Morteza", "m123456789")
print(user)

# db.UpdateData("email", newPassword="0@yahoo.com", user="Fatemeh.fjz", password="0")
# db.UpdateData("email", newEmail="0@yahoo.com", user="Fatemeh.fjz", password="0")
# db.UpdateData("phone", newPhone="012345678", user="Fatemeh.fjz", password="0")


db.DeleteUser(user="Fatemeh.fjz", password="0")


