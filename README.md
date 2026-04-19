# Report-RAG

**Report RAG** is a fully local AI assistant that reads your documents and answers your questions based *only* on the text inside them. Because it runs entirely on your own machine using open-source tools (Ollama and HuggingFace), it is **100% private and free to run**—no data is sent to the cloud, and no API keys are required. 


## Features

* **Local Document Ingestion:** Parses and chunks PDF documents automatically.
* **Local Embeddings:** Uses HuggingFace's `all-MiniLM-L6-v2` model to create fast, local vector embeddings.
* **Vector Storage:** Utilizes FAISS (Facebook AI Similarity Search) for efficient storage and retrieval of document chunks.
* **Local LLM Inference:** Powered by Ollama running the `llama3.2:3b` model, meaning no API keys are required and data never leaves your machine.
* **Interactive UI:** Built with Streamlit for a clean, easy-to-use chat interface.
* **Source Transparency:** Displays the exact retrieved context chunks alongside the generated answer to verify accuracy.

## Tech Stack

* **Frontend:** Streamlit
* **LLM Orchestration:** LangChain
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **Vector Database:** FAISS
* **Local LLM:** Ollama (`llama3.2:3b`)
* **Document Processing:** PyPDFLoader



##  Installation & Setup

1. **Prerequisites:**
   * Install [Ollama](https://ollama.com/) on your system.
   * Pull the Llama 3 model via your terminal: 
     ```bash
     ollama pull llama3.2:3b
     ```
   * Download the `all-MiniLM-L6-v2` embedding model  and place it in a `models` directory relative to your scripts (as referenced in the code), or update the code to use the HuggingFace Hub directly.


## Usage

1. Open the local URL provided by Streamlit (usually `http://localhost:8501`).
2. Type your question regarding the contents of the ingested PDF into the text box.
3. Click "Ask".
4. The application will display the generated answer along with the specific text chunks it retrieved to formulate that answer.
