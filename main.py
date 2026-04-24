from src.loader import load_pdf
from src.chunker import chunk_docs
from src.embeddings import create_vectorstore
from src.graph_workflow import run_graph

# Run once (comment after first run)
docs = load_pdf("data/knowledge.pdf")
chunks = chunk_docs(docs)
create_vectorstore(chunks)

# Query loop
while True:
    query = input("\nAsk your question: ")

    if query.lower() == "exit":
        break

    result = run_graph(query)

    print("\n💬 Answer:", result.get("answer"))
    print("📊 Confidence:", result.get("confidence"))

    if result.get("status") == "escalated":
        print("⚠️ Handled by human agent")