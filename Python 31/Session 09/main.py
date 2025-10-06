# class Files:
#     def __init__(self, address):
#         self.address = address

#     def read(self):
#         file = open(self.address, "r")
#         for l in file.readlines():
#             print(l)
#         file.close()

#     def write(self, add_data):
#         file = open(self.address, "a")
#         file.write(f"{add_data}\n")
#         file.close()

# u = Files("usernames.txt")
# p = Files("passwords.txt")
# username = input("enter your username: ")
# password = input("enter your password: ")
# u.write(username)
# p.write(password)

# p.read()

# file = open("names.txt", "r")

# file.write("Maedeh \n")
# file.write("Shafi \n")
# file.write("Morteza \n")

# print(file.read())

# for l in file.readlines():
#     print(l)

# file.close()

# username = input("enter your username: ")
# try:
#     password = int(input("enter your password: "))
#     u = Files("usernames.txt")
#     p = Files("passwords.txt")

#     u.write(username)
#     p.write(password)
# except:
#     print("invalid password")

# print("end of the script")

import pandas as pd

data = pd.read_excel("data.xlsx", keep_default_na=False, index_col=None)
print(data)

data.at[1, 'password'] = "1253"

print(data["username"][1])

# data.at[1, 'username'] = "Morteza"
# data.at[1, 'password'] = "123"
data.to_excel("data.xlsx", index=False)

# data['password'][0] = 123456789
# data.loc[0, "password"] = 123456789
# data.loc[1, 'username'] = "Maedeh"
# data.loc[1, 'password'] = 123
