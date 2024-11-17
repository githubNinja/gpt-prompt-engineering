import warnings

# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain_openai import OpenAI  # Updated import for OpenAI
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

# Ensure your OpenAI API key is set correctly
os.environ["OPENAI_API_KEY"] = "API_KEY"

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))  # Language Model

style = """American English \
in a calm and respectful tone
"""

# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)
lang_input = input("Enter the language you want to translate to: ")

chain = prompt_template | model
response = chain.invoke({"language": f"{lang_input}", "text": "hi!"})
print(response.content)