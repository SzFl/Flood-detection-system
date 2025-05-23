FROM ollama/ollama:0.6.8

RUN mkdir /OllamaModelfiles

COPY ./Modelfiles /OllamaModelfiles

RUN ollama serve & \
sleep 5 && \
ollama create FloodReader_llama3_8b --file /OllamaModelfiles/FloodReader_llama3_8b.model && \
ollama rm llama3:8b

RUN ollama serve & \
sleep 5 && \
ollama create FloodReader_deepseek-r1_8b --file /OllamaModelfiles/FloodReader_deepseek-r1_8b.model && \
ollama rm deepseek-r1:8b

RUN ollama serve & \
sleep 5 && \
ollama create FloodReader_gemma2_9b --file /OllamaModelfiles/FloodReader_gemma2_9b.model && \
ollama rm gemma2:9b
