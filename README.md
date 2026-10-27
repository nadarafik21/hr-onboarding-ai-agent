# HR Onboarding AI Agent 🤖

### An Agentic AI Assistant for Intelligent HR Onboarding

## 📌 Project Overview

This project focuses on the design and development of an **AI-powered HR onboarding assistant** capable of answering employee questions by intelligently retrieving and processing information from multiple data sources.

Unlike traditional rule-based chatbots, the system leverages **Agentic AI**, combining Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and the Model Context Protocol (MCP) to dynamically select the appropriate tools based on user requests.

The goal is to streamline employee onboarding, improve access to HR information, and reduce repetitive administrative tasks.

## 🚀 Key Features

- **Intelligent Question Answering:** Provides contextual responses to employee HR-related questions using OpenAI LLMs.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from unstructured HR documents through semantic search.
- **MCP Integration:** Enables access to structured employee and organizational data through MCP-based tools.
- **Agentic Workflow:** Uses LangGraph to orchestrate tool selection and manage multi-step interactions.
- **Conversational Memory:** Maintains conversation context across interactions.
- **Performance Evaluation:** Uses LangSmith to analyze execution traces, latency, and token consumption.

## 🛠️ Technologies Used

- **Programming:** Python
- **LLMs:** OpenAI API
- **Agentic AI:** LangChain, LangGraph
- **Retrieval:** RAG, ChromaDB, OpenAI Embeddings
- **Tool Integration:** Model Context Protocol (MCP)
- **Evaluation & Monitoring:** LangSmith
- **Development Environment:** Jupyter Notebook

## 🏗️ System Architecture

The AI agent processes user queries and dynamically determines which tools to invoke:

1. **User Query:** An employee submits an HR-related question.
2. **Agent Reasoning:** The LLM analyzes the request and selects the appropriate tool.
3. **Tool Execution:**
   - RAG retrieves information from HR documents.
   - MCP accesses structured employee or organizational information.
   - The agent can combine tools for complex requests.
4. **Response Generation:** The LLM generates a contextual answer using the retrieved information.
5. **Evaluation:** LangSmith supports monitoring and analysis of agent execution.

## 📊 Evaluation

The agent was evaluated through different HR onboarding scenarios, focusing on:

- Correct tool selection and execution.
- Response relevance and contextual accuracy.
- Execution latency.
- Token consumption.
- Handling of multi-step queries.

## 🔮 Future Improvements

- Deploy the agent through a FastAPI backend.
- Develop an interactive user interface.
- Integrate additional enterprise tools and HR information systems.
- Expand evaluation and monitoring capabilities.
- Improve scalability for real-world organizational environments.

## 📂 Project Notebook

The implementation and experimentation are available in:

**`HR_Onboarding_AI_Agent.ipynb`**

## 👩‍💻 Project Focus

**Generative AI | Agentic AI | LLMs | RAG | MCP | LangChain | LangGraph | Python**

This project demonstrates the integration of LLM-based reasoning, document retrieval, structured data access, and agentic orchestration to address real-world HR information management challenges.
