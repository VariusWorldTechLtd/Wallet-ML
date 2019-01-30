let AWS = require('aws-sdk');
exports.handler = function(event, context, callback) {
  
  console.log("Event: " + JSON.stringify(event));
  let response = {
    "statusCode": 200,
    "body": event.body
  }
  callback(null,response);
}