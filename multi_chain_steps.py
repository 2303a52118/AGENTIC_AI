import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load API key
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

# 2. Create LLM
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# 3. STEP 1 - Generate explanation
prompt1 = ChatPromptTemplate.from_template(
    "Explain the following topic in simple technical terms: {topic}"
)

chain1 = prompt1 | llm | StrOutputParser()

# 4. STEP 2 - Generate key points
prompt2 = ChatPromptTemplate.from_template(
    """
    Convert the following explanation into 5 important
    technical points:

    {explanation}
    """
)

chain2 = prompt2 | llm | StrOutputParser()

# 5. STEP 3 - Generate conclusion
prompt3 = ChatPromptTemplate.from_template(
    """
    Write a short technical conclusion based on the
    following key points:

    {key_points}
    """
)

chain3 = prompt3 | llm | StrOutputParser()

# 6. Take input
topic = input("Enter a technical topic: ")

# 7. Execute the chains
explanation = chain1.invoke({
    "topic": topic
})

key_points = chain2.invoke({
    "explanation": explanation
})

conclusion = chain3.invoke({
    "key_points": key_points
})

# 8. Display results
print("\n========== STEP 1: EXPLANATION ==========")
print(explanation)

print("\n========== STEP 2: KEY POINTS ==========")
print(key_points)

print("\n========== STEP 3: CONCLUSION ==========")
print(conclusion)