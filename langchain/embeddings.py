import openai
import pinecone  # or another vector database


openai.api_key = "YOUR_OPENAI_API_KEY"

# Sample data processing with context embedding
customer_data = [
    "Customer 001 called in for 15 minutes, which is considered a long call.",
    "Customer 002 had a 5-minute IVR session, marked as a short interaction.",
    "Customer 003 used live chat for 10 minutes, which is a moderate duration.",
    "Customer 004 had a 20-minute call with support, marked as a long call."
]



# Initialize Pinecone (or another vector database)
pinecone.init(api_key="YOUR_PINECONE_API_KEY", environment="us-west1-gcp")
index = pinecone.Index("customer_interactions")

# Embed and store each data entry with an identifier
for i, entry in enumerate(customer_data):
    embedding = openai.Embedding.create(input=entry, model="text-embedding-ada-002")["data"][0]["embedding"]
    index.upsert([(f"customer_{i+1}", embedding)])

# Define the question with semantic qualifiers
question = "Retrieve information on customers with a long call duration, strictly over 10 minutes."

# Embed the question to find matching entries
question_embedding = openai.Embedding.create(input=question, model="text-embedding-ada-002")["data"][0]["embedding"]

# Retrieve top matches
result = index.query(vector=question_embedding, top_k=3)
for match in result["matches"]:
    print(f"Retrieved Entry: {customer_data[int(match['id'].split('_')[-1]) - 1]}")
