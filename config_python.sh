#!/bin/bash

PROJECT_PATH="$(pwd)"

PATH_TO_SERVER_SOURCE=$PROJECT_PATH/Server_source

CUSTOM_PATH_FILE=$PATH_TO_SERVER_SOURCE/.venv/lib/python3.10/site-packages/mycustompath.pth

touch $CUSTOM_PATH_FILE
echo $PATH_TO_SERVER_SOURCE > $CUSTOM_PATH_FILE