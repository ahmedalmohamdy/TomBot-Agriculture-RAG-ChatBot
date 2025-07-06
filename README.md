# TomBot - Agriculture RAG ChatBot 🌾🤖

An intelligent agriculture chatbot powered by Retrieval-Augmented Generation (RAG) technology that provides expert advice on farming, crops, and agricultural practices.

## Features

- **Smart Agriculture Assistant**: Get answers to agriculture-related questions
- **PDF Document Processing**: Extracts knowledge from agricultural PDFs
- **Vector Database**: Uses ChromaDB for efficient document retrieval
- **Natural Language Processing**: Powered by Groq's Gemma2-9b-it model
- **Interactive Chat Interface**: User-friendly command-line interface

## Technology Stack

- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for document storage and retrieval
- **Groq API**: Fast inference with Gemma2-9b-it model
- **HuggingFace Embeddings**: all-MiniLM-L6-v2 for text embeddings
- **PyPDF**: PDF text extraction
- **Python**: Core programming language

## Project Structure

```
├── app.py              # Main application entry point
├── chat1.py            # Document processing and vector store setup
├── chat2.py            # LLM setup and retrieval QA chain
├── requirement.txt     # Python dependencies
├── Data/              # Agricultural PDF documents
│   ├── Farming Schemes.pdf
│   ├── Tomato.pdf
│   └── farmerbook.pdf
└── Agriculture_db/    # ChromaDB vector database
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "RAG ChatBot"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## Usage

1. Start the application by running `python app.py`
2. Ask any agriculture-related questions
3. Type 'q' or 'exit' to end the chat session

### Example Interactions

```
🤖 Hello, Ask me Anything About Agriculture or enter q to End Chat
🧑‍🌾 What are the best practices for tomato farming?

🤖 [TomBot provides detailed agriculture advice based on the knowledge base]

🧑‍🌾 You: How do I prevent crop diseases?

🤖 [TomBot gives expert advice on disease prevention]
```

## Key Components

### Document Processing (chat1.py)
- Extracts text from PDF documents
- Splits content into manageable chunks
- Creates vector embeddings using HuggingFace models
- Stores in ChromaDB vector database

### LLM Integration (chat2.py)
- Configures Groq's Gemma2-9b-it model
- Sets up retrieval-based QA chain
- Implements custom prompt template for agriculture focus
- Handles similarity-based document retrieval

### Main Application (app.py)
- Provides interactive chat interface
- Manages conversation flow
- Integrates document retrieval with LLM responses

## Configuration

- **Model**: Gemma2-9b-it (via Groq API)
- **Max Tokens**: 512
- **Temperature**: 0.1 (for consistent responses)
- **Chunk Size**: 500 characters
- **Chunk Overlap**: 100 characters
- **Similarity Threshold**: 0.6

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Add your license information here]

## Support

For questions or support, please contact the Ahmed Almohamdy.

---

**Developed with ❤️ by Ahmed Almohamdy**
