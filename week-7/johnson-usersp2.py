# ==============================================
# ; Title: johnson_usersp2.py
# ; Author: Caitlynne Johnson
# ; Date: 24 April 2023
# ; Description: Learning how to use Python to connect to MongoDB part 2

# =============================================

#import the MongoClient
from pymongo import MongoClient

#build a connection string to connect to
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.x3pcqyt.mongodb.net/web335DBretryWrites=true&w=majority")

print(client)

#variable to access the web335DB
db = client['web335DB']

#create a new user document 
caitlynne = {
    "firstName": "Caitlynne",
    "lastName": "Johnson",
    "employeeId": "1016",
    "email": "cjohnson@gmail.com",
    "dateCreated": datetime.datetime.utcnow()
}

#insert the document into the users collection 
caitlynne_user_id = db.users.insert_one(caitlynne).inserted_id
print(caitlynne_user_id)

#prove the insert worked by searching for the document
print(db.users.find_one({"employeeId": "1016"}))

#update query to change the user's email address 
db.users.update_one(
    {"employeeId": "1016"},
    {
        "$set": {
            "email": "caitjohnson@gmail.com"
        }
    }
)

#proving the update worked by searching the collection for the user by employeeId
print(db.users.find_one({"employeeId": "1016"}))

#query to delete the user document just made above
result = db.users.delete_one({
    "employeeId": "1013"
})

#display the results of the query
print(result)

#prove the query worked by searching the collection for the deleted document
print(db.users.find_one({"employeeId": "1016"}))

