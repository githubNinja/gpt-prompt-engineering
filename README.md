# gpt-prompt-engineering


### Instructions on installation
Step 1: Ensure the Virtual Environment is Activated
1. Activate your virtual environment manually in the terminal.
    #### if you’re on Linux/macOS:
    source path/to/your/.venv/bin/activate

2. After activating the virtual environment, confirm it’s active by checking if the prompt changes to include (.venv) or by running:

3. which python

4. Install the Dependencies in this active environment if they aren’t there:
    #### pip install langchain langchain-openai langgraph pyautogen
5. To install a specific dependency only from requirements.txt 
    #### pip install -r requirements.txt --no-deps langchain_community


## Running docker Compose
* docker-compose up
* Verify OpenSearch is Running: Check if OpenSearch is running by accessing it on http://localhost:9200. You should see a JSON response indicating OpenSearch is up
## Install Open Search Client
* Install OpenSearch Python Client: Install the Python client for OpenSearch:
* pip install opensearch-py
