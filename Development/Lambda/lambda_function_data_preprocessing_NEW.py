from __future__ import print_function

import base64

print('Loading function')


def lambda_handler(event, context):
    output = []
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

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}