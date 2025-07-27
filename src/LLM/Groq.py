from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


# GroqLLM class to interact with Groq's LLM service
# It uses the ChatGroq client to send prompts and receive responses.
class GroqLLM:
    def __init__(self):
        # Initialize the Groq client with the API key from environment variables
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.1-8b-instant",
            max_retries=3,
            timeout=60,
        )
    
    def get_llm(self):
        """
        Returns the Groq client instance.
        This method is used to access the Groq client for sending prompts.
        """
        return self.llm
