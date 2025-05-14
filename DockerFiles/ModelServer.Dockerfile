FROM ollama/ollama:0.6.8

RUN mkdir /OllamaModelfiles

COPY ./Modelfiles /OllamaModelfiles

RUN ollama serve & \
sleep 5 && \
ollama create FloodReader --file /OllamaModelfiles/FloodReader.model

# RUN ollama serve & \
# ollama rm llama3:8b