import os

import openai
from opensearchpy import OpenSearch
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

api_key = "api_key"
os.environ["OPENAI_API_KEY"] = api_key

# Connect to OpenSearch
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin")  # adjust if authentication is enabled
)

# Step 1: Generate an embedding for the question
#question = "Retrieve information for customers who had issues with their phone."
question = "Customer called to inquire about account balance and recent transactions, give me complete customer details"
question_embedding_response = openai.embeddings.create(
    model="text-embedding-ada-002",
    input=question
)
question_embedding = question_embedding_response.data[0].embedding

# Step 2: Retrieve relevant records from OpenSearch
query = {
    "size": 5,  # Number of top results to retrieve
    "query": {
        "knn": {
            "embedding": {
                "vector": question_embedding,
                "k": 10  # Number of nearest neighbors
            }
        }
    }
}

# Search
response = client.search(index="customer_data", body=query)

# Extract the relevant customer records
retrieved_records = [hit["_source"] for hit in response["hits"]["hits"]]

# Combine retrieved information into a context string
context = "\n".join([f"Customer ID: {record['customer_id']}, Notes: {record['notes']}" for record in retrieved_records])

# Step 3: Generate a conversational response using LangChain
# Initialize the chat model
chat_model = ChatOpenAI(model_name="gpt-4")

# Define a prompt template with context
prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are a helpful assistant with access to customer interaction data.

    Customer Interaction Data:
    {context}

    Based on the above information, answer the following question:
    Question: {question}
    Answer:
    """
)

# Initialize LangChain's LLM chain with the prompt and chat model
llm_chain = LLMChain(llm=chat_model, prompt=prompt_template)

# Run the LLM chain with the retrieved context and question
answer = llm_chain.invoke({"context": context, "question": question})
print(type(answer))  # Check if it's a dictionary, string, or custom object
print(answer.get("text"))        # Display the entire structure
print(answer)

