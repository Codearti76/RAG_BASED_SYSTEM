from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def create_vectorstore(chunks):
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="vectorstore"
    )

    return db