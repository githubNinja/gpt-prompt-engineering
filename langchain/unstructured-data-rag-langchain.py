import warnings
from langchain_openai import OpenAI  # Import OpenAI from langchain_openai
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import os

# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] ="KEY" # Replace with your actual API key

# Initialize the OpenAI LLM with the API key
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Load and read the unstructured text file
with open("customer_data.txt", "r") as file:
    customer_data = file.read()

# Define a prompt template for searching based on a question
# Here, we structure the prompt to include customer data and the question
prompt_template = """
Given the following customer data:

{customer_data}

Answer the question based on the information above.
Question: {question}
Answer:
"""

# Create the prompt template and LLM chain
prompt = PromptTemplate(
    input_variables=["customer_data", "question"],
    template=prompt_template
)
llm_chain = prompt | llm

# Define a question based on the pattern you want to search for
question = "Retrieve information for customers whose call duration is greater than 10 minutes (i.e., strictly more than 10 minutes)."


# Use `invoke` to query the LLM chain
answer = llm_chain.invoke({"customer_data": customer_data, "question": question})
print(answer)
