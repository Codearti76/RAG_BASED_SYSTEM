from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_docs(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100
    )
    return splitter.split_documents(documents)