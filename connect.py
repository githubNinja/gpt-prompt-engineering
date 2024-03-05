import psycopg2
import openai
import pandas as pd
from openai import OpenAI

# Connect to PostgreSQL
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


OPENAI_API_KEY='YOUR OPEN API KEY'
openai.api_key = OPENAI_API_KEY
client = OpenAI()


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)

# Fetch data into a Pandas DataFrame
query = "SELECT * FROM linear_regression2;"
data = pd.read_sql_query(query, conn)
print("table data::", data)
# Close the connection
conn.close()

data_column = data.loc[1]['y']
print(f"column value is::{data_column}")

# Call the OpenAI API for chat completion
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Find the value of Z based on the X=2 and Y=212 values",
        },
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
# Extract the generated response from the OpenAI API
gen_response = response.choices[0].message.content
print(f"My prediction for Z based on the model is::{gen_response}")

# Append the machine learning model prediction to the OpenAI response
#model_response = f"My prediction for Z based on the model is {response}. " + response.choices[0].message.content


