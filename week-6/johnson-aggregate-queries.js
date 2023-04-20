/**
 * Title: johnson-aggregate-queries.js
 * Author: Caitlynne Johnson
 * Date: 19th April 2023
 * Description Executing more MongoDB queries and experimenting with aggregate queries.
 */

// query that shows a list of documents in the houses collection
db.houses.find()

// query that shows a list of documents in the students collection
db.students.find()

// query that adds a document to the student's collection
students = {"firstName": "Caitlynne", "lastName": "Johnson", "studentId": "s1019", "houseId": "h1009"}

// query that inserts the user object that was previously created above
db.students.insertOne(students)

// query that proves the document was added to the user's collection
db.students.find({ lastName: "Johnson" })

//query that deletes the document previously created
db.students.deleteOne({"_id": ObjectId("64407b6263dc22ea969ccb81")})

// query that proves it was deleted
db.students.find({ lastName: "Johnson" })

// query that shows a list of students by house 
db.houses.aggregate([ { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "studentsHousing", }, }, ]);

// query that shows a list of students from house Gryffindor 
db.houses.aggregate([ { $match: { mascot: "Lion", }, }, { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "studentsHousing", }, }, ]);

// query that shows a list of students for the Eagle mascot
db.houses.aggregate([ { $match: { mascot: "Eagle", }, }, { $lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "studentsHousing", }, }, ]);