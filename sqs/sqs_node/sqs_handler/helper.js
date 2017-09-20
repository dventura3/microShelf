var sendFailure = function(res, err){
    res.writeHead(404, { "Content-Type" : "application/json" });
    res.end(JSON.stringify({ "msg" : err }));
}

var sendSuccess = function(res, data){
    res.writeHead(200, {"Content-Type": "application/json"});
    res.end(JSON.stringify({ "msg" : data }));
}

exports.sendResponse = function(res, err, data) {
    if(err) {
        sendFailure(res, err);
        return console.log(err);
    }
    else {
    	sendSuccess(res, data);
    	return console.log(data);
    }
}