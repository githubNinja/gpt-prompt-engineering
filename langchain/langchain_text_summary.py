import warnings

from langchain_core.prompts import PromptTemplate

# Suppress all LangChain deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from langchain_openai import OpenAI  # Updated import for OpenAI
import os
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"
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

customer_transcript = """[{"message":"Persistent Menu, options: - Main Menu","participant":"CompanyX.ABC","seq_num":1,"timestamp":"2024-01-16T18:19:38.000Z","type":"bot"},{"message":"file: https://https://amazon.com","participant":"CompanyX.ABC","seq_num":2,"timestamp":"2024-01-16T18:19:38.000Z","type":"bot"},{"message":"Hi! This is the Fricano ABC XYZ Virtual Assistant. I can help with any of the following topics or answer other common questions.","participant":"CompanyX.ABC","seq_num":3,"timestamp":"2024-01-16T18:19:38.000Z","type":"bot"},{"message":"How can I help you today?","participant":"CompanyX.ABC","seq_num":4,"timestamp":"2024-01-16T18:19:38.000Z","type":"bot"},{"message":"<<far fa-money-check-alt>> Auto Pay","participant":"Web chat visitor","seq_num":5,"timestamp":"2024-01-16T18:19:49.000Z","type":"consumer"},{"message":"Below are some common questions related to Auto Pay.","participant":"CompanyX.ABC","seq_num":6,"timestamp":"2024-01-16T18:19:50.000Z","type":"bot"},{"message":"Can I pick a date for my Auto Pay payment?","participant":"Web chat visitor","seq_num":7,"timestamp":"2024-01-16T18:19:58.000Z","type":"consumer"},{"message":"Auto Pay payments will always pull on your due date or the first available business day following your due date when your due date falls on a weekend or holiday. Currently you cannot select the date for Auto Pay payments.","participant":"CompanyX.ABC","seq_num":8,"timestamp":"2024-01-16T18:19:58.000Z","type":"bot"},{"message":"If you’d like to request a change to your payment due date you can do so.","participant":"CompanyX.ABC","seq_num":9,"timestamp":"2024-01-16T18:19:58.000Z","type":"bot"},{"message":"<<far fa-home>> Main Menu","participant":"Web chat visitor","seq_num":10,"timestamp":"2024-01-16T18:20:36.000Z","type":"consumer"},{"message":"Can I help you with anything else?","participant":"CompanyX.ABC","seq_num":11,"timestamp":"2024-01-16T18:20:37.000Z","type":"bot"},{"message":"No, Thanks","participant":"Web chat visitor","seq_num":12,"timestamp":"2024-01-16T18:20:57.000Z","type":"consumer"},{"message":"Sorry, I'm struggling to understand... You can try restating your question or browse within the topics below.","participant":"CompanyX.ABC","seq_num":13,"timestamp":"2024-01-16T18:20:58.000Z","type":"bot"},{"message":"Done","participant":"Web chat visitor","seq_num":14,"timestamp":"2024-01-16T18:21:16.000Z","type":"consumer"},{"message":"My apologies, I'm having issues understanding.","participant":"CompanyX.ABC","seq_num":15,"timestamp":"2024-01-16T18:21:17.000Z","type":"bot"},{"message":"Let me get you to an agent for further assistance.","participant":"CompanyX.ABC","seq_num":16,"timestamp":"2024-01-16T18:21:17.000Z","type":"bot"},{"message":"Transferring you to an agent...","participant":"CompanyX.ABC","seq_num":17,"timestamp":"2024-01-16T18:21:17.000Z","type":"bot"},{"message":"How would you rate your experience?","participant":"CompanyX.ABCSurvey","seq_num":18,"timestamp":"2024-01-16T18:21:33.000Z","type":"bot"},{"message":"","participant":"CompanyX.ABCSurvey","seq_num":19,"timestamp":"2024-01-16T18:21:33.000Z","type":"bot"}]"""

response = summarization_chain.invoke({"conversational_text": customer_transcript})
print(f"summary:\n {response}")
