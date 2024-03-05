import openai
from openai import OpenAI

# Your OpenAI API key
OPENAI_API_KEY='OPENAI_API_KEY'
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# The machine learning code for house price prediction
ml_code = """
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Generate some random data for demonstration
np.random.seed(0)
house_sizes = np.random.randint(1000, 3000, 100)
house_prices = 50 * house_sizes + 50000 + np.random.normal(0, 10000, 100)

# Reshape the data to make it compatible with scikit-learn
X = house_sizes.reshape(-1, 1)
y = house_prices

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Let's make a prediction for a new house size
new_house_size = np.array([[2000]])
predicted_price = model.predict(new_house_size)
print(f"Predicted price for a house with size {new_house_size[0][0]}: ${predicted_price[0]:,.2f}")

# Plot the data and the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red', linewidth=3)
plt.xlabel('House Size (sq ft)')
plt.ylabel('House Price ($)')
plt.title('Simple Linear Regression Example')
plt.show()
"""

# User prompt for the AI chat completion
user_prompt = """
You are a helpful assistant that can predict house prices. 
Given a house size, you should provide the predicted price.
Let's test it with a house size of 2000 sq ft.
"""

# Combine the user prompt and the machine learning code
full_code = user_prompt + ml_code

# Use the OpenAI API to generate a chat completion
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant that can predict house prices."},
        {"role": "user", "content": "Given a house size, you should provide the predicted price."},
        {"role": "assistant", "content": ml_code},
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Extract the assistant's reply from the API response
assistant_reply = response.choices[0].message.content

# Print the assistant's reply
print(assistant_reply)
