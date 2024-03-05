import psycopg2
import pandas as pd
import openai

# Connect to PostgreSQL
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

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


# Assuming 'target_column' is the column you want to predict
#X = data.drop('target_column', axis=1)
X = data[['x']]
print("X data::", X)
Y = data[['y']]
print("Y data::", Y)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X, Y)


openai.api_key = 'your open API Key'
# Replace 'prompt_text' with the prompt you want to generate
prompt_text = f"tell me a joke"
print('prompt_text::', prompt_text)


response = openai.Completion.create(
    engine="gpt-3.5-turbo",
    prompt=prompt_text,
    max_tokens=100,
    n=1,
    stop=None,
)

prediction = response['choices'][0]['text']
print(f"Model Prediction: {prediction}")