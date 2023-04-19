# ==============================================
# ; Title: johnson_usersp1.py
# ; Author: Caitlynne Johnson
# ; Date: 19 April 2023
# ; Description: Learning how to use Python to connect to MongoDB

# =============================================

#import the MongoClient 
from pymongo import MongoClient

#build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.x3pcqyt.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)

#variable to access the web335DB
db = client['web335DB']

#displays a list of all documents in the users collection
for user in db.users.find():
    print(user)
    
#displays the document of an employee's id
print(db.users.find_one({"employeeId": "1011"}))

#displays the document with the employee's last name
print(db.users.find_one({"lastName": "Mozart"}))