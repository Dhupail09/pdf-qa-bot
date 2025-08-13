PDF Q&A Bot
A simple, interactive web app built with Streamlit that allows users to upload PDF documents, ask questions, and receive instant answers using a Large Language Model (LLM).

**(1)Features**
 PDF Upload — Upload any PDF document.

 Question Answering — Ask specific questions about the PDF content.

 LLM Integration — Uses Google's Gemini API for intelligent answers.

 Efficient Search — Leverages FAISS vector database for fast retrieval.

 User-Friendly UI — Minimal and clean interface using Streamlit.

**(2)Tech Stack**
Frontend: Streamlit

Backend: Python

Embedding Model: HuggingFace sentence-transformers

Database: FAISS

API: Google Gemini

Environment Variables: python-dotenv

**(3)How It Works****
PDF Upload

User uploads a PDF file.

Text Extraction

Extracts and cleans text from the PDF.

Embedding Generation

Uses HuggingFace to convert text chunks into vector embeddings.

Vector Storage

Stores embeddings in FAISS for efficient similarity search.
**
**User Query****

User asks a question about the document.

Relevant Chunk Retrieval

FAISS finds the most relevant sections of the PDF.

**LLM Response**

Gemini API processes the retrieved content and generates a final answer.

(4)Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/YourUsername/pdf-qa-bot.git
cd pdf-qa-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Environment Setup
**Create a .env file in the root directory:**

ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
Run the App
bash
Copy
Edit
streamlit run app.py

**Example Usage**
Upload your PDF.

Ask: "Summarize the first chapter"

The bot will extract relevant text and answer using the LLM.

Folder Structure
bash
Copy
Edit
Option to save chat history

Model selection (Gemini, OpenAI, etc.)

Summarization mode

