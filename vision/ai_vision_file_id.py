from openai import OpenAI
import os


os.environ["OPENAI_API_KEY"] = "api_key"
client = OpenAI()

# Function to create a file with the Files API
def create_file(file_path):
  with open(file_path, "rb") as file_content:
    result = client.files.create(
        file=file_content,
        purpose="vision",
    )
    return result.id

# Getting the file ID
file_id = create_file(os.path.join(os.path.dirname(__file__), '../images/john_deere_2630_old.png'))

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[{
        "role": "user",
        "content": [
            #{"type": "input_text", "text": "what's in this image?"},
            {"type": "input_text", "text": "can you identify the 2 defects in this image and provide a quick"
                                           "summary and confirm what would be the resale value of this model now ?"},
            {
                "type": "input_image",
                "file_id": file_id,
            },
        ],
    }],
)

print(response.output_text)
