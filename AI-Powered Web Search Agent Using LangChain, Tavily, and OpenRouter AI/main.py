from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

# OpenRouter LLM
llm = ChatOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    model=os.getenv("MODEL_NAME"),
    temperature=0
)

# Tavily Search
search = TavilySearch(max_results=5)

print("====================================")
print("   AI WEB SEARCH ASSISTANT")
print("====================================")
print("Type 'exit' to quit.")

while True:

    question = input("\nAsk Anything: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    # Search the web
    results = search.invoke(question)

    # Create prompt
    prompt = f"""
You are an AI Research Assistant.

Use the following web search results to answer the user's question.

Web Search Results:
{results}

User Question:
{question}

Instructions:
- Use the web search information.
- Give an accurate answer.
- Keep the answer clear and easy to understand.
- Do not invent information.
"""

    try:
        # Generate answer
        response = llm.invoke(prompt)

        print("\nAnswer:")
        print(response.content)

    except Exception as e:
        print("\nUnable to generate the answer.")
        print("Error:")
        print(e)