# create_embeddings.py
import openai
from opensearchpy import OpenSearch

# Connect to OpenSearch
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin")  # adjust if authentication is enabled
)

# Set up OpenAI API key
openai.api_key = "api_key"
# Sample customer data
customer_data = [
    {
        "customer_id": "001",
        "name": "John Doe",
        "channel": "Call Center",
        "interaction_type": "Call",
        "date": "2023-10-15",
        "duration": 15,
        "rag_status": "Green",
        "notes": "Customer called to inquire about account balance and recent transactions."
    },
    {
        "customer_id": "002",
        "name": "Charles Brown",
        "channel": "Call Center2",
        "interaction_type": "Chat",
        "date": "2023-11-15",
        "duration": 22,
        "rag_status": "Red",
        "notes": "Customer called to inquire about a fraud transaction."
    }
    # Add more customer records as needed
]


# Extract the notes from each customer record to create a list of texts
notes_list = [customer["notes"] for customer in customer_data]

# Create embeddings for all customer notes in a single API call
embedding_response = openai.embeddings.create(
    model="text-embedding-ada-002",
    input=notes_list
)

# Define the index name
index_name = "customer_data"

for record in customer_data:  # records: List of customer records
    embedding = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=record["notes"]
    ).data[0].embedding
    record["embedding"] = embedding
    client.index(index="customer_data", body=record)



# Assign each embedding to the corresponding customer record
# for i, customer in enumerate(customer_data):
#     customer["embedding"] = embedding_response.data[i].embedding

# # Print the customer data with embeddings
# for customer in customer_data:
#     print(f"Customer ID: {customer['customer_id']}, Embedding: {customer['embedding']}")

#notes = "Customer called to inquire about account balance and recent transactions."

#
# Generate embeddings and store data in OpenSearch
# for customer in customer_data:
#     embedding_response = openai.embeddings.create(
#         model="text-embedding-ada-002",
#         # input=customer["notes"],
#         input=notes)
# embedding = embedding_response.data[0].embedding
# print(embedding)

#Prepare the document with embedding
# document = customer.copy()
#document["embedding"] = embedding

# #Index the document in OpenSearch
# response = client.index(index=index_name, body=document)
# print(f"Indexed customer {customer['customer_id']}: {response['result']}")
