#!/bin/bash
set -e
set -x

# pull proper image
docker pull ollama/ollama:0.6.8

# started image/made container
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ContainerToImage ollama/ollama:0.6.8

# copied Modelfile to container
docker exec ContainerToImage mkdir -p /Ollama
docker cp ./Modelfiles/FloodReader.model  ContainerToImage:/Ollama/FloodReader.model

# make model based on Modelfile
docker exec ContainerToImage ollama create FloodReader --file /Ollama/FloodReader.model

# delete model based on which our is
docker exec ContainerToImage ollama rm llama3:8b

# stoping ContainerToImage
docker stop ContainerToImage

exit 0