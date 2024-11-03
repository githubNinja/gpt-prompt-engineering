# This code is for v1 of the openai package: pypi.org/project/openai
import openai
from openai import OpenAI

# The key is part of my githubkran account
OPENAI_API_KEY =  ''
openai.api_key = OPENAI_API_KEY
client = OpenAI()
#"content": "based on the temperature given suggest clothing: 55F"

response = client.chat.completions.create(
 # model="gpt-3.5-turbo",
  model = "gpt-4o",
  messages=[
    {
      "role": "user",
      "content": "Give me latest news on US presidental election ?"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
prediction = response.choices[0].message.content
print('response:', prediction)