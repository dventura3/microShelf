const fs = require('fs');
const aws = require('aws-sdk');
const Helper = require('./helper');
const credentials_config = JSON.parse(fs.readFileSync('./config/shelves_config.json', 'utf8'));


/* --------------- Amazon SQS ------------------- */

const queueURL = "HERE";
// id of the last message got by the microservice
let receipt = "";


// __dirname 
aws.config.loadFromPath('./config/aws_config.json');

const sqs = new aws.SQS();



/* --------------- Controller ------------------- */

exports.setLockersProperties = function(req, res) {

    // const data = req.body;


    var params = {
      QueueUrl: 'HERE',
      ReceiptHandle: receipt
    };

    sqs.deleteMessage(params, function(err, data) {
        if (err) {
            console.log(err, err.stack);
            Helper.sendResponse(res, err, null);
        }
        else {
            console.log(data);
            Helper.sendResponse(res, null, data);
        }
    });
}


exports.setLockerProperty = function(req, res){

    const lockerID = req.params.lockerID;
    //add try-catch
    //const data = req.body;

    Helper.sendResponse(res, null, data);
}


exports.openAllLockers = function(req, res) {

    var params = {
        MessageBody: 'Test MessageBody',
        QueueUrl: 'HERE',
        DelaySeconds: 0
    };

    sqs.sendMessage(params, function(err, data) {
        if (err) {
            console.log('Error');
            console.log(err, err.stack);
            Helper.sendResponse(res, err, null);
        }
        else {
            console.log('ok');
            console.log(data);
            Helper.sendResponse(res, null, data);
        }
    });
}



exports.openAllLockersForShelf = function(req, res) {

    const shelfID = req.params.shelfID;
    console.log('>> shelfID: ' + shelfID);

    var params = {
      QueueUrl: 'HERE',
      VisibilityTimeout: 600 // 10 minutes wait for anyone else to process
    };

    sqs.receiveMessage(params, function(err, data) {
        if (err) {
            console.log(err, err.stack);
            Helper.sendResponse(res, err, null);
        }
        else {
            console.log(data);
            receipt = data.Messages[0].ReceiptHandle;
            Helper.sendResponse(res, null, data);
        }
    });
}