var aws=require("aws-sdk");aws.config.region=process.env.AWS_REGION||"us-east-1";var step=new aws.StepFunctions,sns=new aws.SNS;function stop(){return getExecution().then(result=>result&&"RUNNING"===result.status?step.stopExecution({executionArn:result.executionArn,cause:"ALEXA manual stop"}).promise().then(()=>"Current Job has been stopped"):"there is no job to stop")}function start(){return getExecution().then(result=>result&&"RUNNING"===result.status?"A job is currently executing":sns.publish({Message:"{}",TopicArn:process.env.START_TOPIC}).promise().then(()=>"A new job has been started"))}function getInfo(){return getExecution().then(info=>step.getExecutionHistory({executionArn:info.executionArn,reverseOrder:!0}).promise().then(history=>{if(info.stopDate)return`The latest job ended in status ${info.status}, was started at ${date(info.startDate)}, and ended at ${date(info.stopDate)}`;var step=history.events.map(x=>{return Object.keys(x).map(y=>x[y].name).find(y=>y)}).filter(x=>x)[0];return`the current job was started at ${date(info.startDate)}, is in state ${info.status}, and the current step is ${step?step.replace(/([a-z])([A-Z])/g,"$1 $2"):"not known"}`}))}function getStatus(){return getExecution().then(result=>{if(result)var message=`Your job is in state ${result.status}`;else message="You have not run any jobs";return message})}function getExecution(){return step.listExecutions({stateMachineArn:process.env.STEPFUNCTION_ARN}).promise().then(result=>result.executions[0])}function date(string){var d=new Date(string);return`${d.toUTCString().match(/(.*, \S* \S*)/)[1]} at ${d.toUTCString().match(/.*, \S* \S* \S* (\S*:\S*):.*/)[1]} UTC`}function Response(callback,end=!1){return function(message){callback(null,{version:"1.0",sessionAttributes:{},response:{outputSpeech:{type:"PlainText",text:message},shouldEndSession:end}})}}exports.handler=function(event,context,callback){console.log(JSON.stringify(event,null,2));var response=Response(callback);try{if("LaunchRequest"===event.request.type)response("Welcome to sagebuild, you can start,stop or get the status of your build by saying start, stop, status, or info");else if("IntentRequest"===event.request.type)switch(event.request.intent.name){case"AMAZON.CancelIntent":case"AMAZON.StopIntent":stop().then(response);break;case"AMAZON.HelpIntent":response("You can start, stop or get the status of your build by saying start, stop, or status");break;case"Start":start().then(response);break;case"Status":getStatus().then(response);break;case"Info":getInfo().then(response)}else"SessionEndedRequest"===event.request.type&&callback(null)}catch(e){console.log(e),callback(e)}};