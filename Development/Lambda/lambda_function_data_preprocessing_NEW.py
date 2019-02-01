import os
import io
import boto3
import json
import csv
import pandas as pd

print('Preprocessing data')

df = pd.read_json(event)

df.convert_objects(convert_numeric=True)
df.fillna(0, inplace=True)

def handle_non_numerical_data(df):
    columns = df.columns.values
    
    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]
        
        # print(column,df[column].dtype)
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            
            column_contents = df[column].values.tolist()
            # finding just the uniques
            unique_elements = set(column_contents)
            #great, found them
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    # creating dict that contains new
                    # id per unique string
                    text_digit_vals[unique] = x
                    x+=1
                    
            # now we map the new "id" value
            # to replace the string
            df[column] = list(map(convert_to_int, df[column]))
            
    return df

df = handle_non_numerical_data(df)
event = df.to_json(orient='index')

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    
    data = json.loads(json.dumps(event))
    payload = data['data']
    print(payload)
    
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)
    pred = int(result['predictions'][0]['score'])
    predicted_label = 'M' if pred == 1 else 'B'
    
    return predicted_label