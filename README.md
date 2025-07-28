# Agentic Blog Generation Project

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103+-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)

An AI-powered blog generation system that creates SEO-optimized content with multilingual support, built with FastAPI and LangChain.

## Features

- **AI-Powered Content Generation**
  - Automatic blog title creation
  - Detailed content generation
  - SEO optimization built-in

- **Multilingual Support**
  - English (default)
  - French
  - Hindi
  - Urdu
  - Arabic
  - Russian
  - German
  - Pashto

- **Technical Highlights**
  - LangGraph workflow orchestration
  - Groq LLM integration (Llama 3)
  - Pydantic data validation
  - FastAPI REST endpoints

## Getting Started

### Prerequisites
- Python 3.12+
- Groq API key (free tier available)
- Poetry (recommended) or pip

### Installation
```bash
git clone https://github.com/Abubakar0011/Agentic-BlogGeneration.git
cd Agentic-BlogGeneration
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
echo "GROQ_API_KEY=your_api_key_here" > .env
echo "LANGCHAIN_API_KEY=your_langsmith_key_here" >> .env

## Usage
### Start server:
```bash
uvicorn app:app --reload
```

### API Endpoint:
```bash
POST /blogs
{
  "topic": "AI Future",
  "language": "french"  # optional
}
```

```bash
POST /blogs
{
  "topic": "AI Future",
  "language": "french"  # optional
}


## Project Structure
```text
src/
├── States/           # Data models
├── LLM/              # Groq integration
├── Nodes/            # LangGraph nodes
└── Graph/            # Workflow logic
app.py                # FastAPI app

