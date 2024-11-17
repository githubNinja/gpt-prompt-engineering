from opensearchpy import OpenSearch

# Connect to OpenSearch
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_auth=("admin", "admin")  # adjust if authentication is enabled
)

# Define the index mapping with vector fields
index_name = "customer_data"
mapping = {
    "settings": {
        "index": {
            "knn": True  # Enable k-Nearest Neighbor search
        }
    },
    "mappings": {
        "properties": {
            "customer_id": {"type": "keyword"},
            "name": {"type": "text"},
            "channel": {"type": "keyword"},
            "interaction_type": {"type": "keyword"},
            "date": {"type": "date"},
            "duration": {"type": "integer"},
            "rag_status": {"type": "keyword"},
            "notes": {"type": "text"},
            "embedding": {
                "type": "knn_vector",
                "dims": 1536  # Set the dimensionality based on your embedding model
            }
        }
    }
}

# Create the index
#client.indices.create(index=index_name, body=mapping)
print(f"Index '{index_name}' created with vector fields.")
