from typing import TypedDict
from pydantic import BaseModel, Field


class Blog(BaseModel):
    """
    Represents the state of a blog post.
    """
    title: str = Field(..., description="The title of the blog post")
    content: str = Field(..., description="The content of the blog post")


class BlogState(TypedDict):
    """
    Represents the state of the blog.
    """
    topic: str
    blog: Blog
    current_language: str
