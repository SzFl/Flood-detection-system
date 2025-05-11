#!/bin/bash
set -e

# pull proper image
docker pull ollama/ollama:0.6.8

# started image/made container
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name container_to_image ollama/ollama:0.6.8

# copied Modelfile to container
docker exec container_to_image mkdir -p /Ollama
docker cp ./Modelfiles/FloodReader.model  container_to_image:/Ollama/FloodReader.model

# make model based on Modelfile
docker exec container_to_image ollama create FloodReader --file /Ollama/FloodReader.model

# stoping container_to_image
docker stop container_to_image

# building image based on container_to_image
docker commit container_to_image flood-reader:1.0