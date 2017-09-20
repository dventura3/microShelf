/* External libraries */
const express = require('express'),
    fs = require('fs'),
	bodyParser = require('body-parser');

/* Internal libraries */
var CtrlSQS = require('./sqs_handler/sqs-ctrl');


/* --------------- Server Configuration ------------------- */

var SERVER_PORT = 5300;
var app = express();


/* --------------- Routes ------------------- */


app.post("/api/lockers/all/:shelfID", CtrlSQS.openAllLockersForShelf);

app.post("/api/lockers/all", CtrlSQS.openAllLockers);

app.post("/api/lockers/:lockerID", CtrlSQS.setLockerProperty);

app.post("/api/lockers", CtrlSQS.setLockersProperties);

/* --------------- Launch Service ------------------- */
app.listen(SERVER_PORT);

module.exports = app

console.log("Server running on port " + SERVER_PORT);