# SQL Doctor

AI-powered SQL database analyzer using RAG (Retrieval-Augmented Generation). Upload your SQL schema files and get instant explanations, queries, and insights about your database structure.

## Features

- Analyze SQL database schemas using natural language
- Get detailed explanations of tables, relationships, and queries
- Generate SQL queries from plain English questions
- Support for multiple database files
- Interactive CLI interface

## Prerequisites

- Python 3.8+
- MistralAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/sql-doctor.git
cd sql-doctor
```

2. Create virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
MISTRAL_API_KEY=your_api_key_here
BASE_URL=your_base_url_here
MISTRAL_MODEL=your_model_name_here
```

5. Add SQL files to `db/` folder

## Usage

1. Run the application:
```bash
python sql-doctor.py
```

2. Select a database file from the list

3. Ask questions about your database:
```
Apa saja tabel yang ada di database ini?
Bagaimana cara membuat query untuk mengambil semua user?
Jelaskan hubungan antara tabel orders dan customers
```

4. Type `/q`, `/exit`, or `/quit` to exit

## Project Structure

```
sql-doctor/
├── db/                 # SQL schema files
├── venv/               # Virtual environment
├── .env                # Environment variables (not committed)
├── requirements.txt    # Python dependencies
└── sql-doctor.py       # Main application
```

## How It Works

1. **Document Loading**: SQL files are loaded and split into chunks
2. **Embeddings**: Text chunks are converted to vector embeddings using MistralAI
3. **Vector Store**: Embeddings are stored in ChromaDB for fast retrieval
4. **RAG Pipeline**: User questions retrieve relevant context and generate responses

## Technologies

- [LangChain](https://github.com/langchain-ai/langchain) - LLM framework
- [ChromaDB](https://github.com/chroma-core/chroma) - Vector database
- [MistralAI](https://mistral.ai/) - LLM and embeddings

## License

MIT"# SQL-Doctor" 
