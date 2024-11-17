import warnings

from langchain_core.prompts import PromptTemplate

# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain_openai import OpenAI  # Updated import for OpenAI
import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "API_KEY""
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))  # Language Model

model = ChatOpenAI(model="gpt-4o-mini-2024-07-18")



template_format = """
    return "You are a helpful AI bot.You are a summarization expert.Summarize the following
    customer call transcription in a concise manner."""


prompt_template = PromptTemplate(
    input_Variables=["conversational_text"],
    template=template_format
)

summarization_chain = prompt_template | llm

customer_transcript = """Put all the Content here that you want to summarize"""

response = summarization_chain.invoke({"conversational_text": customer_transcript})
print(f"summary:\n {response}")
