import os
import warnings

from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI


# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# Ensure your OpenAI API key is set correctly
os.environ["OPENAI_API_KEY"] = "API_KEY"
 # Replace this or set the environment variable in your system
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Example1 start .......................
'''
prompt = "What is a langchain conversational and how it can help"
model = "gpt-4o"

#def process_prompt(prompt, model):
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model=model,
)
   # return  response.choices[0].message["content"]


print(f"response::{response.choices[0].message.content})")

# Example1 end  .......................
'''


# Example2 start .......................
customer_style = """American English \
in a calm and respectful tone
"""

customer_text = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need your help \
right now, matey!
"""


template_string = f"""Translate the text \
that is delimited by triple backticks \
into a style that is {customer_style}. \
text: ```{customer_text}```
"""


prompt_template = ChatPromptTemplate.from_template(template_string)

customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_text)

print(customer_messages[0].content)

#
# import os
# from openai import OpenAI
#
# client = OpenAI(
#     api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="gpt-4o",
# )


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

# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,
#     )
#     return response.choices[0].message["content"]
#
#
# def get_chat_completion():
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Say this is a test",
#             }
#         ],
#         model="gpt-4o",
#     )


# # Use the `create` method under `openai.ChatCompletion`
# response = OpenAI.ChatCompletion.create(
#     model="gpt-4",
#     messages=[
#         {"role": "user", "content": "Hello, how are you?"}
#     ]
# )
#
# # Extract the assistant's reply
# print(response['choices'][0]['message']['content'])

#get_completion("What is 1+1?")