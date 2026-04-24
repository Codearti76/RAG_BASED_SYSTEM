from src.retriever import get_retriever
from src.llm import get_llm

retriever = get_retriever()
llm = get_llm()
def run_rag(query):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a customer support assistant.
    Answer ONLY from the context below.

    Context:
    {context}

    Question:
    {query}
    """

    try:
        response = llm.invoke(prompt)
        answer = response.content if hasattr(response, "content") else str(response)
    except Exception as e:
        answer = "Error generating response"
        print("LLM ERROR:", e)

    confidence = 0.9 if docs else 0.2

    return {
        "answer": answer,
        "confidence": confidence,
        "docs": docs
    }