from pydantic import BaseModel, Field


# Models
class Blog(BaseModel):
    """Represents the state of a blog post."""
    title: str = Field(default="", description="The title of the blog post")
    content: str = Field(default="", description="The content of the blog post")


class BlogState(BaseModel):
    """Represents the state of the blog."""
    topic: str
    blog: Blog = Blog()
    current_language: str = "english"
