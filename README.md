# Description of project

## Purpose

This project analise text messages and classify them on messages that talk about flood and not. Additionally, if message is classified as flood it extract additional informations. This allows to detect currently happening floods and events relative to it.

This is a prof of concept.

## Structure and technologies

Project was build as element of ETL process. It is a Pyhon script that sends request with a message to Ollama server which run on docker. Ollama manages 3 models:
- llama3_8b
- deepseek-r1_8b
- gemma2_9b

Each of them is customized to return structure output. Structure output is a output from any ollama model in form of a JSON file. Models are forced to return this kind of output and it allow easier handling for python script.

# Setup

1. In folder Analysis run 'python3 -m venv .venv'
2. In folder "Server_source" run: 'python3 -m venv .venv'
3. Enter it with 'source ./Server_source/.venv/bin/activate' 
4. Then run 'pip install -r ./Server_source/requirements.txt'
5. Run 'bash config_python.sh' while being in main project folder.
6. VS code might still have a problem with proper configuring terminal and python virutual environment with atribute 'python.defaultInterpreterPath'(from .vscode/settings.json) to './Server_source/.venv/bin/activate' because it did not exist. Try exit VS code and start it from main folder again. It should work.
7. Create in folder './Server_source' file .env and set it's variables with proper values:

- TWEETER_BEARER_TOKEN - this requires creation of acconut on (https://developer.x.com/en). Then user should create a app and set his variable with a token bearer provided by tweeter.

8. Start Ollama docker container with 'docker-compose up'.

**Warning** generating docker image may take a while due to the size of models.

# How to use it

In folder Server_source there is a file pipe_main.py that can be customize to get proper pipeline. User can specify loaders that loads data from rss, kaggle, tweeter etc. and pipe stages to manage how messages should be handled. At the end user should get folder and with result.csv file. This ouput fllders can be abalise by jupyter notebook file in folder Analysis. This notebook compares results of models.

