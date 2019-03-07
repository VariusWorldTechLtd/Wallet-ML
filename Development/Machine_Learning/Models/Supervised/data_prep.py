import pandas as pd 
import numpy as np 

df = pd.read_csv('Gambling Background.csv')

df.drop(['Timestamp', 'VWT Privacy Policy'], axis=1, inplace=True)

df.rename(columns={"Yearly income (in £'s)": 'Yearly income', "Monthly disposable income (in £'s)": 'Disposable income', 
                        "Average monthly spend on gambling (in £'s)": 'Gambling spend', 'Are you a regular smoker?': 'Smoker',
                        'Do you take drugs regularly?': 'Drugs', 'How much alcohol do you consume a week?': 'Alcohol consumption',
                        'At what age did you first gamble for money?': 'First gambling age',
                        'Do you have friends who gamble?': 'Friends gamble', 'Did your parents gamble regularly?': 'Parents gamble', 
                        'Have you bet more than you can afford to lose?': 'PGSI Q1', 
                        'Have you needed to gamble with larger amounts of money to get the same feeling of excitement?': 'PGSI Q2', 
                        'When you gambled, did you go back another day to try and win back the money you lost?': 'PGSI Q3', 
                        'Have you borrowed money or sold anything to get money to gamble?': 'PGSI Q4', 
                        'Have you felt that you might have a problem with gambling?': 'PGSI Q5', 
                        'Has gambling caused you any health problems, including stress or anxiety?': 'PGSI Q6', 
                        'Have people criticised your betting or told you that you had a gambling problem, regardless of whether or not you thought it was true?': 'PGSI Q7', 
                        'Has your gambling caused any financial problems for you or your household?': 'PGSI Q8', 
                        'Have you felt guilty about the way you gamble or what happens when you gamble?': 'PGSI Q9'}, inplace=True)


# # If all categorical variables available are not in the dataset these functions must be used
# df.replace(['Never', 'Sometimes', 'Most of the time', 'Almost always'], [0, 1, 2, 3], inplace=True)

print(df)


# This only works for datasets if all the available categorical variables are inplace
def handle_non_numerical_data(df):
    
    # handling non-numerical data: must convert.
    columns = df.columns.values

    for column in columns:
        text_digit_vals = {}
        def convert_to_int(val):
            return text_digit_vals[val]

        #print(column,df[column].dtype)
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            
            column_contents = df[column].values.tolist()
            #finding just the uniques
            unique_elements = set(column_contents)
            # great, found them. 
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    # creating dict that contains new
                    # id per unique string
                    text_digit_vals[unique] = x
                    x+=1
            # now we map the new "id" vlaue
            # to replace the string. 
            df[column] = list(map(convert_to_int,df[column]))

    return df

df = handle_non_numerical_data(df)

# for i in range(0,9):

df['Problem Gambler'] = df['PGSI Q1'] + df['PGSI Q2'] + df['PGSI Q3'] + df['PGSI Q4'] + df['PGSI Q5'] + df['PGSI Q6'] + df['PGSI Q7'] + df['PGSI Q8'] + df['PGSI Q9']

print(df)

df.drop(['PGSI Q1', 'PGSI Q2', 'PGSI Q3', 'PGSI Q4', 'PGSI Q5', 'PGSI Q6', 'PGSI Q7', 'PGSI Q8', 'PGSI Q9'], axis=1, inplace=True)

df[df['Problem Gambler'] > 8] = 1




print(df)
