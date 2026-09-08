from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model=os.getenv("MODEL_NAME"),
    temperature=0
)

# Store conversation histories
store = {}


def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# Chat model with memory
conversation = RunnableWithMessageHistory(
    llm,
    get_session_history
)


print("=== Conversational Memory Chatbot ===")
print("Type 'exit' to stop.\n")

while True:
    question = input("You : ")

    if question.lower() == "exit":
        break

    response = conversation.invoke(
        question,
        config={
            "configurable": {
                "session_id": "sravan"
            }
        }
    )

    print("AI  :", response.content)