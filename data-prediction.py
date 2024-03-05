import openai
import pandas as pd
from sklearn.linear_model import LinearRegression
from openai import OpenAI


OPENAI_API_KEY='OPENAI_API_KEY'
openai.api_key = OPENAI_API_KEY
client = OpenAI()
# Load your modeled data
data = {'X': [1, 2, 4], 'Y': [12, 212, 9], 'Z': [12, 424, 36]}
df = pd.DataFrame(data)

# Train your machine learning model (using scikit-learn as in the previous example)
model = LinearRegression()
X_train = df[['X', 'Y']]
y_train = df['Z']
model.fit(X_train, y_train)

# Define your conversation with the user
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "assistant", "content": "I can help you with predictions."},
]


# Function to get the model's response
def get_openai_response(prompt):
    # Combine the conversation history with the user's prompt
    #conversation = conversation_history + [{"role": "user", "content": prompt}]

    # Extract user input
    user_input = prompt.split()  # Assuming the user input includes X and Y values
    print("split value:::", user_input)

    context = "remember value of Z is X * Y. As an example if X is 3 and Y is 18 then Z is 54"

    prompt = prompt + context
    print(f"prompt value with context:::{prompt}")
    # Predict Z using the machine learning model
    x_input = int(user_input[0])
    y_input = int(user_input[1])
    z_prediction = model.predict([[x_input, y_input]])[0]

    # Call the OpenAI API for chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                #"content": "Find the value of Z based on the X and Y values, remember value of Z is X * Y. if X is 3 "
                         #  "and Y is 18 then Z is 54. Also give me a integer value"
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


# Example usage
#user_prompt = "What is the value of X when Y is 212?"
user_prompt = "2 12"
full_response = get_openai_response(user_prompt)
print("Full Response:", full_response)
