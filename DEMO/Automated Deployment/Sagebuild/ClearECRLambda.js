var response=require("cfn-response"),aws=require("aws-sdk");aws.config.region=process.env.AWS_REGION;var cb=new aws.CodeBuild,s3=new aws.S3,ecr=new aws.ECR,lambda=new aws.Lambda;exports.handler=function(event,context,callback){console.log(JSON.stringify(event,null,2)),"Delete"===event.RequestType?new Promise(function(res,rej){var token;!function next(){ecr.listImages({repositoryName:event.ResourceProperties.repo,nextToken:token}).promise().then(function(result){return ecr.batchDeleteImage({imageIds:result.imageIds,repositoryName:event.ResourceProperties.repo}).promise().then(function(){result.nextToken?(token=result.nextToken,setTimeout(()=>next(),500)):res()})}).catch(rej)}()}).then(()=>response.send(event,context,response.SUCCESS)).catch(x=>{console.log(x),response.send(event,context,response.SUCCESS)}):response.send(event,context,response.SUCCESS)};