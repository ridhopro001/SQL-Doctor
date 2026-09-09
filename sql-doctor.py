from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings,ChatMistralAI
from langchain_chroma import Chroma
import os

print(f"\nSQL DOCTOR")
print(f"Dibuat oleh : https://github.com/ridhopro001\n\n")
def RAG(db_selected) :
    selected = TextLoader(".\db/" + db_selected, encoding="utf-8").load()
    
    # 1. PERBAIKAN: Perbesar chunk_size agar skema CREATE TABLE tidak terpotong
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=300).split_documents(selected)
    
    embbedings = MistralAIEmbeddings()
    
    # 2. PERBAIKAN: Gunakan ephemeral / in-memory DB & hapus collection lama jika ada
    db = Chroma.from_documents(
        documents=splitter,
        embedding=embbedings,
        collection_name="sql_rag_temp"
    )
    
    # 3. PERBAIKAN: Naikkan nilai 'k' agar lebih banyak tabel/skema yang terbawa
    retriever = db.as_retriever(
        search_kwargs={"k" : 5}
    )
    
    # 4. PERBAIKAN: Ubah temperature ke 0.0 untuk hasil yang presisi dan konsisten
    llm = ChatMistralAI(
            base_url=os.getenv("BASE_URL"),
            api_key=os.getenv("MISTRAL_API_KEY"),
            model_name=os.getenv("MISTRAL_MODEL"),
            temperature=0.0
        )
    
    # Bagian sistem pertanyaan
    while True :
        question = input("Pertanyaan : ")
        
        if (question == "/q") or (question == "/exit") or (question == "/quit") :
            print(f"Sampai nanti ~")
            break
        
        else :
            docs = retriever.invoke(question)
    
            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )
            
            prompt = f"""
            You are an expert SQL assistant. Answer the question based ONLY on the provided RAG context below.

            <context>
            {context}
            </context>

            CRITICAL SCHEMA RULES:
            1. STRICT COLUMN & TABLE NAMES: You MUST ONLY use the exact table and column names explicitly defined in the <context>.
            2. NO INVENTING/HALLUCINATING: Do NOT assume, invent, modify, or add any column names (e.g., adding '_ID', 'CREATED_AT', or renaming columns) even if they seem standard or logical.
            3. CASE SENSITIVITY: Match the exact spelling and casing of tables and columns as shown in the schema within <context>.

            INSTRUCTIONS:
            1. Answer strictly based on the provided context. If the query cannot be formed due to missing schema information, explicitly state that the context does not provide sufficient table/column information.
            2. If the user's question asks for code (SQL queries, functions, scripts, etc.):
            - Provide the complete SQL code snippet using ONLY valid context columns.
            - Explain each section/part of the SQL code in detail so the user understands its functionality.
            3. ALWAYS respond in the exact same language used in the user's question.

            Question:
            {question}
            """
            
            response = llm.invoke(prompt)
            
            print("_"*100)
            print(response.content)
            print("_"*100)
            
        
        
    
    
    
    
    
    




# Bagian memilih database
db_opsi = []
db_opsi_num = []

def semua_nama_file() :
    lokasi = Path(".\db")

    print("Semua database : ")
    for index,file in enumerate(lokasi.iterdir(),start=1) :
        if file.is_file() :
            file_name = file.name.split(".")[-1]
            if (file_name == "sql") or (file_name == "SQL" ) :
                db_opsi.append(file.name)
                db_opsi_num.append(index)
                print(f"{index}. {file.name}")
            

while True :
    print("_"*100)
    semua_nama_file()
    print("_"*100)
    
    user_db_selected = input(f"\nPilih nomor database : ")

    if (user_db_selected == "/q") or (user_db_selected == "/exit") or (user_db_selected == "/quit") :
        print(f"Sampai nanti ~")
        break

    elif int(user_db_selected) in db_opsi_num :
        RAG(db_opsi[int(user_db_selected) - 1])
        break

    else :
        print(f"Maaf nomor database tidak tersedia")
