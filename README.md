
# 🤖 RAG-Based Customer Support Assistant (LangGraph + HITL)

## 📌 Overview

This project is a **Retrieval-Augmented Generation (RAG)** based Customer Support Assistant that answers user queries using a PDF knowledge base and intelligently escalates complex queries using **Human-in-the-Loop (HITL)**.

It combines **vector search + LLM + workflow control** to build a reliable and scalable AI system.

---

## 🚀 Features

- 📄 PDF-based knowledge retrieval
- 🔍 Semantic search using embeddings
- 🤖 Context-aware answer generation
- 🔁 Workflow control using LangGraph
- 👨‍💻 Human-in-the-Loop (HITL) escalation
- ⚡ Fast responses using Groq LLM

---

## 🧠 How It Works

1. Load PDF knowledge base  
2. Split into chunks  
3. Convert text into embeddings  
4. Store embeddings in ChromaDB  
5. User query → embedding  
6. Retrieve relevant chunks  
7. LLM generates answer  
8. Confidence check:
   - High → return answer  
   - Low → escalate (HITL)

---

## 🏗️ System Architecture


User Query
↓
LangGraph Workflow
↓
Retriever → ChromaDB
↓
LLM (Groq)
↓
Answer / HITL


---

## 🧩 Tech Stack

- **LangChain** – RAG pipeline  
- **LangGraph** – Workflow & decision-making  
- **ChromaDB** – Vector database  
- **HuggingFace** – Embeddings  
- **Groq API** – LLM inference  



## ⚙️ Setup Instructions

### 1️⃣ Clone Repo


2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Environment Variables

Create .env file:

GROQ_API_KEY=your_api_key_here
5️⃣ Run Project
python main.py
🧪 Sample Queries
What is refund policy?
How to cancel order?
I want to file a fraud complaint
🔁 HITL (Human-in-the-Loop)

If:

Confidence is low
Query is sensitive

👉 System escalates to human agent

⚠️ Challenges
Choosing optimal chunk size
Improving retrieval accuracy
Handling workflow state
🚀 Future Improvements
Multi-document support
Chat memory
Web interface (Streamlit)
Feedback learning system

👨‍💻 Author
Aarti Chopade
AI Internship Project

📌 Conclusion

This project demonstrates how RAG + workflow orchestration + human intervention can be combined to build reliable real-world AI systems.
