# 🧠 Local PDF Embedding Pipeline with Ollama + Chroma

This project lets you convert PDF files into vector embeddings using the `mxbai-embed-large:335m` 
model via [Ollama](https://ollama.com/), and stores them in a local [Chroma](https://www.trychroma.com/) 
vector database — all running in Docker.

---

## 📦 Components

- **Ollama**: Local LLM backend for embedding using `mxbai-embed-large:335m`
- **ChromaDB**: Local vector store for semantic search
- **Python script**: Extracts text from PDF, generates embeddings, stores vectors

---

## 🚀 Quick Start

### 1. Clone this repo

```bash
git clone https://your-repo-url
cd your-repo


2. Place a PDF file
Place your target PDF in the project directory (e.g., your.pdf).

3. Start Ollama + Chroma
Make sure Docker is installed and running.

Then launch both services:

docker compose up -d


after this :
docker exec -it ollama bash
ollama pull mxbai-embed-large:335m

check chromaDB is working:
http://localhost:8000/api/v2/heartbeat


4. Install Python dependencies:
``
pip install -r requirements.txt (OR) pip install ollama chromadb pypdf
``
requirements.txt should include:
pypdf
chromadb
ollama

5. Run the embedding script Edit the PDF filename in the script if needed, then run:
``
python pdf_to_chroma.py
``
6. finaly check the data in DB use this script
``
python pdf_to_chroma.py

``