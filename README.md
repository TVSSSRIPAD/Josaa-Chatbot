### Josaa-Chatbot
- Simple RAG based chat-bot to chat about IIT seat allocations based on past data.
- This chatbot is developed as part of my experimentation with LLMs.
- Currently data from 2023, 2024 from all IITs is being used.
- Data is parsed from [Joint Seat Allocation Authority aka JOSAA's official website](https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx)
- Reference blog used - [Ollama embedding models](https://ollama.com/blog/embedding-models)

### Tech Stack:-
- Chroma DB as Vector Store.
- UV for dependency management
- Ollama to run embedding model, primary LLM
- [`nomic-embed-text:latest`](https://ollama.com/library/nomic-embed-text) embedding model for creating vector embedding
- [`gemma3:12b`](https://ollama.com/library/gemma3) as primary LLM

### Ollama commands used:-
- `ollama pull nomic-embed-text`
- `ollama list`
- `ollama run gemma3:12b`
- `ollama -v`
- `ollama pull gemma3:12b`
