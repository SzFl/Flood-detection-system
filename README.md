
# Description of project

Project that uses AI models as element of ETL process.

# Setup

All steps needs to be done to work on project.

# Python

1. In folder "Server_source" run: 'python3 -m venv .venv'
2. Run 'bash config_python.py' while being in main project folder.
3. Enter it with 'source ./Server_source/.venv/bin/activate' 
4. Then run 'pip install -r ./Server_source/requirements.txt'
5. VS code might still have a problem with proper configuring terminal and python virutual environment with atribute 'python.defaultInterpreterPath'(from .vscode/settings.json) to './Server_source/.venv/bin/activate' because it did not exist. Try exit VS code and start it from main folder again. It should work.
6. Create in folder './Server_source' file .env and set it's variables with proper values:

- TWEETER_BEARER_TOKEN - this requires creation of acconut on (https://developer.x.com/en). Then user should create a app and set his variable with a token bearer provided by tweeter.

## Docker

1. Just run 'docker-compose up'.

