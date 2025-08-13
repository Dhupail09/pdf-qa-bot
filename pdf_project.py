import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai

# this to load the .env file to access the API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialising the Genai and Choosing model version 
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

#  using streamlit 
# thse are sidebar contents  
with st.sidebar:
    st.title("Welcome to Dhupail's LLM chat app")
    st.markdown('''
    ## About  
    This app is an LLM-powered chatbot built using:  
    - [Streamlit](https://streamlit.io/)  
    - [Langchain](https://python.langchain.com/)  
    - [Genai](https://aistudio.google.com/apikey) LLM model  
    ''')
    add_vertical_space(1)
    st.write("[Made by Dhupail Ahmadhu J](https://github.com/Dhupail09)")


st.set_page_config(page_title="PDF Q&A with Gemini", layout="centered")
st.title("Ask Questions from your PDF")

uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")
user_question = st.text_input("Ask a question based on the PDF:")

if uploaded_pdf and user_question:
    # Step 1: Read PDF
    reader = PdfReader(uploaded_pdf)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text() or ""
     
   # st.write(raw_text)


    # 2 we are splitting the text into the chunk of 1000 character almost 200-300 words 
    # using the recursive syntax splitting them into chunks 
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_text(raw_text)
    #st.markdown("The chun thek of pdf")
   #st.write(chunks)

     #extracting a pretrained model from Huggingface 
    # using similarity check (similarites between the ques and stored ans)
    embeddings = HuggingFaceEmbeddings()
    chunk_embeddings = embeddings.embed_documents(chunks)

    st.subheader("🔢 Chunk Embeddings (Preview)")
    for i, (chunk, emb) in enumerate(zip(chunks, chunk_embeddings)):
        st.markdown(f"**Chunk {i+1}:**\n{chunk[:200]}...")
        st.text(f"Embedding (768-d vector, first 10 dims shown):\n{emb[:10]}")
        st.markdown("---")
    #vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    #st.markdown("Emedding")
    #st.write(embeddings)


    # Step 4: Search for relevant context
    docs = vectorstore.similarity_search(user_question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    #st.write(context)
    #relevant answer if need 
    #st.markdown("The relevant answer is:")
    #st.write(context)

    # Step 5: Ask Gemini
    prompt = f"""
#You are a helpful assistant. Based on the following PDF content:

#{context}

#Answer this question: {user_question}

#"""
#here is the error handling block (if anything goes wrong ...!!!!)
    try:
        response = model.generate_content(prompt)
        st.markdown("### Answer:")
        st.write(response.text.strip())
    except Exception as e:
        st.error(f" Error from Gemini: {str(e)}")
