/**
 * Title: johnson-mongodbshell.js
 * Author: Caitlynne Johnson
 * Date: 9th April 2023
 * Description Queries for Assignment 4.2 MongoDB Shell
 */

// displays all documents in the users collection
db.users.find()

// searches user with an email that matches the input
db.users.find({email: "jbach@me.com"})

// searches users that matches the input
db.users.find({lastName: "Mozart"})

//searches for user with the first name that matches the input
db.users.find({firstName: "Richard"})

//searches for user with the employeeID that matches the input
db.users.find({employeeId: "1010"})