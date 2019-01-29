# S3 prefix
prefix = 'DEMO-scikit-byo-iris'

# Define IAM role
import boto3
import re

import os
import numpy as np
import pandas as pd
from sagemaker import get_execution_role

role = get_execution_role()

# Create the session
import sagemaker as sage
from time import gmtime, strftime

sess = sage.Session()

# Upload the data for training
WORK_DIRECTORY = 'data'

data_location = sess.upload_data(WORK_DIRECTORY, key_prefix=prefix)

# Create Estimator
account = sess.boto_session.client('sts').get_caller_identity()['Account']
region = sess.boto_session.region_name
image = '{}.dkr.ecr.{}.amazonaws.com/sagemaker-decision-trees:latest'.format(account, region)

tree = sage.estimator.Estimator(image,
                       role, 1, 'ml.c4.2xlarge',
                       output_path="s3://{}/output".format(sess.default_bucket()),
                       sagemaker_session=sess)

tree.fit(data_location)

# Deploy model
from sagemaker.predictor import csv_serializer
predictor = tree.deploy(1, 'ml.m4.xlarge', serializer=csv_serializer)

# Choose some data and use it for a prediction
shape=pd.read_csv("data/iris.csv", header=None)

import itertools

a = [50*i for i in range(3)]
b = [40+i for i in range(10)]
indices = [i+j for i,j in itertools.product(a,b)]

test_data=shape.iloc[indices[:-1]]

print(predictor.predict(test_data.values).decode('utf-8'))


# Transform job (could be used for assessing gambling behaviour)
transform_output_folder = "batch-transform-output"
output_path="s3://{}/{}".format(sess.default_bucket(), transform_output_folder)

transformer = tree.transformer(instance_count=1,
                               instance_type='ml.m4.xlarge',
                               output_path=output_path)


transformer.transform(data_location, content_type='text/csv', split_type='Line')
transformer.wait()

# Read results from S3 files and print output
s3_client = sess.boto_session.client('s3')
s3_client.download_file(sess.default_bucket(), "{}/iris.csv.out".format(transform_output_folder), '/tmp/iris.csv.out')
with open('/tmp/iris.csv.out') as f:
    results = f.readlines()   
print("Transform results: \n{}".format(''.join(results)))