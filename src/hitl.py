def escalate_to_human(query):
    print("\n⚠️ Escalating to human agent...")

    # Simulated human response
    human_response = input("👨‍💻 Human agent reply: ")

    return {
        "answer": human_response,
        "status": "escalated",
        "confidence": 1.0
    }