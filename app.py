import uvicorn
from fastapi import FastAPI, HTTPException, Request
from src.Graph.graph_builder import GraphBuilder
from src.LLM.Groq import GroqLLM

import os
from dotenv import load_dotenv

from src.States.blogstate import Blog, BlogState

load_dotenv()
app = FastAPI()

print(os.getenv("LANGCHAIN_API_KEY"))

os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# API endpoint to generate blog content


@app.post("/blogs")
async def generate_blog(request: Request):
    data = await request.json()
    topic = data.get("topic")
    language = data.get("language", "english").lower()

    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required")

    # Import the pre-compiled graph
    from src.Graph.graph_builder import graph

    # Prepare initial state
    initial_state = {
        "topic": topic,
        "current_language": language,
        "blog": {
            "title": "",
            "content": ""
        }
    }

    # Invoke the graph
    try:
        result = graph.invoke(initial_state)
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
