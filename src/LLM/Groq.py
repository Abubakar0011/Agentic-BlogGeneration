from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


class GroqLLM:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        
        self.llm = ChatGroq(
            api_key=api_key,
            model="llama3-8b-8192",
            max_retries=3,
            timeout=60,
        )
    
    def get_llm(self):
        """Returns the Groq client instance."""
        return self.llm

