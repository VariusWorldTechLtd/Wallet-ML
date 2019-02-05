# Architecture

![Step Functions Framework](StepFunction_&_CloudWatch_Framework.jpg)

## Overview

This folder contains the javascript code of functions that can be used within the step functions. For example, the CreateTrainingJob file contains all code to train a new model and save the output.

## Template

The follwoing URL links to a tutorial on creating a CloudFormation Stack which should contain all services needed for the updating and redeployment. Note that this not only works using Step Functions and CloudWatch but also services within the SageMaker architecture.

https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/