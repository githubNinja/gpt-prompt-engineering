from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # Assuming you're using OpenAI's model

template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate(input_variables=["product"], template=template)


llm = ChatOpenAI(openai_api_key="OPENAPI_KEY")  # Replace with your OpenAI API key

llm_chain = LLMChain(prompt=prompt, llm=llm)

product = "eco-friendly cleaning products"
response = llm_chain.run(product)
print(f"response is::", response)




