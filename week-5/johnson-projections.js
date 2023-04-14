/**
 * Title: johnson-projections.js
 * Author: Caitlynne Johnson
 * Date: 14th April 2023
 * Description Applying the $project operation in our queries.
 */

//query that adds a new user to the collection
user = {"firstName": "Gustav", "lastName": "Mahler", "employeeId": "1013", "email": "gmahler@menubar.com", "dateCreated": new Date()}

//this inserts the user object that was previously created above
db.users.insertOne(user)

//query that updates a users info
db.users.update({employeeId: "1009" }, { $set: { email: "mozart@me.com" } });

//query to prove the user's information was updated
db.users.find({ lastName: "Mozart" })

//query to list all documents in a user's collections
db .users.find({}, { firstName: 1, lastName: 1, email: 1 });