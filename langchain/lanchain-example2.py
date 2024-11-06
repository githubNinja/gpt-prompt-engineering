import warnings

# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain_openai import OpenAI  # Updated import for OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import os

# Ensure your OpenAI API key is set correctly
os.environ["OPENAI_API_KEY"] = "KEY"

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")) # Language Model


# Create a prompt template and LLM chain
prompt = PromptTemplate(input_variables=["input_text"], template="Translate this to French: {input_text}")
llm_chain = prompt | llm
# Example usage with `invoke` instead of `predict`
question = "What is the meaning of life?"
answer = llm_chain.invoke({"input_text": question})  # Updated method to `invoke`
print(answer)




