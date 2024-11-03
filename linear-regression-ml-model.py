import numpy as np
import openai
import pandas as pd
from sklearn.linear_model import LinearRegression
from openai import OpenAI
import seaborn as sns
from sklearn.model_selection import train_test_split

# OPENAI_API_KEY='OPENAI_API_KEY'
OPENAI_API_KEY = ''
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# Load your modeled data
# how to read a file present in a folder

cData = pd.read_csv("content/auto-mpg.csv")
print("print head::{}", cData.shape)
df = pd.DataFrame(cData)
print("cDATA Head::{}", cData.head())

# dropping/ignoring car_name
# cData = cData.drop('car name', axis=1)
# Also replacing the categorical var with actual values
cData['origin'] = cData['origin'].replace({1: 'america', 2: 'europe', 3: 'asia'})
print('cData:{}', cData['origin'])

# Create Dummy variables

cData = pd.get_dummies(cData, columns=['origin'])
cData.head()

# Summary
cData.describe()

# dTYPES
print('cData.dtypes::{}', cData.dtypes)

# isdigit()? on 'horsepower'
## Checking if 'horsepower' column values are digits
hpIsDigit = pd.DataFrame(cData.horsepower.str.isdigit(),
                         columns=['horsepower'])  # if the string is made of digits store True else False

# print isDigit = False!
non_numeric_hp = cData[hpIsDigit['horsepower'] == False]  # from temp take only those rows where hp has false
print(non_numeric_hp)

# Treat Missing values
cData = cData.replace('?', np.nan)
cData[hpIsDigit['horsepower'] == True]

var = cData[hpIsDigit['horsepower'] == False]

print('describe:{}', cData.describe())

# Drop the car name field
cData.drop(columns=['car name'], inplace=True)
cData.head()

# replace the missing values with median value.
# Note, we do not need to specify the column names below
# every column's missing value is replaced with that column's median respectively  (axis =0 means columnwise)
# cData = cData.fillna(cData.median())

medianFiller = lambda x: x.fillna(x.median())
cData = cData.apply(medianFiller, axis=0)

cData['horsepower'] = cData['horsepower'].astype(
    'float64')  # converting the hp column from object / string type to float
print('cData.dtypes:{}', cData.dtypes)

print('cData.head:{}', cData.head())

# Split Data

# lets build our linear model
# independant variables
X = cData.drop(['mpg', 'origin_europe'], axis=1)
# the dependent variable
y = cData[['mpg']]

cData.head()

#  Build Linear Model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# Fit Linear Model

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

y_pred = regression_model.predict(X_test)
print("predictions on dataset::", y_pred)

# mpg,cylinders,displacement,horsepower,weight,acceleration,model year,origin,car name

user_query = "what is the predicted car mileage with 0 cylinders with 150 displacement, 100 horse power, 2800 weight"

# Define your conversation with the user
conversation_history = [
    {"role": "system", "content": "You are a assistant that helps to predict car mileage based on the user provided "
                                  "car features."},
    {"role": "assistant", "content": user_query},
]


# Function to get the model's response
def get_openai_response(prompt):
    print(f"prompt value with context:::{prompt}")

    # Call the OpenAI API for chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Append the machine learning model prediction to the OpenAI response
    model_response = response.choices[0].message.content

    return model_response


user_prompt = user_query

full_response = get_openai_response(user_prompt)
print("Full Response:", full_response)
