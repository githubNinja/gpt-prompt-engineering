import os

# Ensure your OpenAI API key is set correctly
os.environ["OPENAI_API_KEY"] = "key" # Replace this or set the environment variable in your system



#openai.api_key = OPENAI_API_KEY

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
# OR for chat models:



# Initialize the GPT-4 model (adjust model name to your version, e.g., "gpt-4")
# llm = OpenAI(model_name="gpt-4")
#
# # Define a prompt template
# prompt = PromptTemplate(
#     input_variables=["question"],
#     template="You are a helpful assistant. Answer the question: {question}"
# )
#
# # Create an LLM chain
# llm_chain = LLMChain(llm=llm, prompt=prompt)
#
# # Run the chain with a question
# question = "What are the benefits of using LangChain with GPT-4?"
# response = llm_chain.run(question)
#
# print("Response:", response)


# Use the `create` method under `openai.ChatCompletion`
response = OpenAI.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Extract the assistant's reply
print(response['choices'][0]['message']['content'])