# AGENTIC_AI

This repository contains implementations and practical experiments related to **Agentic AI using LangChain**. The experiments focus on building AI agents, integrating external tools, managing conversational memory, and performing real-time web search.
## 📦 Required Libraries

The experiments in this repository use the following Python libraries:

- `langchain` – Framework for building LLM applications and agents
- `langchain-core` – Core LangChain components
- `langchain-community` – Community integrations
- `langchain-openai` – OpenAI-compatible LLM integration
- `langchain-tavily` – Tavily web search integration
- `python-dotenv` – Loading environment variables from `.env`
- `openai` – OpenAI-compatible API client

### Installation

Install all required dependencies using:

```bash
pip install -r requirements.txt
## 📚 Experiments

### Building a Simple Question-Answering Agent Using LangChain

A basic AI agent is developed using LangChain to understand user queries and generate appropriate responses using an LLM.

**Technologies:**
- Python
- LangChain
- OpenRouter AI
- LLM

---

### AI-Powered Web Search Agent Using LangChain, Tavily, and OpenRouter AI

A real-time web search agent is developed by integrating the Tavily Search Tool with a LangChain agent and OpenRouter AI.

**Technologies:**
- Python
- LangChain
- Tavily Search
- OpenRouter AI
- NVIDIA Nemotron-3 Ultra 550B Free

**Key Concepts:**
- Tool Calling
- LangChain Agents
- Web Search
- Real-Time Information Retrieval

---

### Conversational Memory Management Using LangChain and OpenRouter AI

A conversational AI agent is developed with memory management to maintain and use previous conversation history during interactions.

**Technologies:**
- Python
- LangChain
- OpenRouter AI
- Conversational Memory

**Key Concepts:**
- Conversation History
- Memory Management
- Context Preservation
- Conversational AI

## 🛠️ Technologies Used

- Python
- LangChain
- OpenRouter AI
- Tavily
- LLMs
- AI Agents
- Tool Calling
- Conversational Memory

## 📁 Repository Structure

```text
AGENTIC_AI/
│
├── README.md
├── .gitignore
│
├── Building a Simple Question-Answering Agent Using LangChain/
│   └── qa_agentic.py
│
├── AI-Powered Web Search Agent Using LangChain, Tavily, and OpenRouter AI/
│   └── main.py
│
└── Conversational Memory Management Using LangChain and OpenRouter AI/
    └── main.py
