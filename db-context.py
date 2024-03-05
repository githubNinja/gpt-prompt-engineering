# import sys
import openai
import psycopg2
from openai import OpenAI

OPENAI_API_KEY = 'Specify your OPEN API Key'
openai.api_key = OPENAI_API_KEY
client = OpenAI()
db_result = ""
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "assistant", "content": "I can help you with predictions."},
]

db_connection_string = {
    "host": "127.0.0.1",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "mysecretpassword"
}


def get_user_name_details():
    global db_result
    conn = psycopg2.connect(**db_connection_string)
    cursor = conn.cursor()
    # query = f"SELECT * FROM test_user WHERE username=\'{user_name}\'"
    query = f"SELECT * FROM test_user"
    cursor.execute(query)
    does_this_work = "(1, 'Jeff', None)" + "(2, 'Brian', None)"
    print(f"does this work::{does_this_work}")
    result = cursor.fetchall()
    for row in result:
        print(f"row is :{str(row)} and db_result is::{db_result}")
        db_result += str(row)

    print(f"result from db::{db_result}")
    cursor.close()
    conn.close()
    return result


def get_openai_response(prompt, context):
    prompt = f"{prompt} {context}"
    # print(f"prompt value with context:::{prompt}")

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


# user_input = sys.argv[1]
# user_input = "Brian"
# print(f"Name of the user:{user_input}")
user_name_details = get_user_name_details()
context = (f"The postgresql table test_user contains 3 columns. User id and user name and address. The data set contains data with "
           f"user id, user name and address as follows ::{user_name_details}. Not all user names have address. if address field is None then the user doesnt have address")
#prompt = "Who is living in Atlanta ?"
prompt = "Does Brad have an address to live ? and how many users are existing in the data set and who lives in Davenport ?"
full_response = get_openai_response(prompt, user_name_details)
print("Full Response:", full_response)
