from src.States.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.States.blogstate import Blog
from langgraph.graph import END


# Nodes
class BlogNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState) -> dict:
        """Create the title for the blog."""
        if state.topic:
            prompt = """You are an expert blog content writer. Use Markdown formatting. 
                      Generate a blog title for the {topic}. This title should be creative and SEO friendly"""
            system_message = prompt.format(topic=state.topic)
            response = self.llm.invoke(system_message)
            return {"blog": {"title": response.content}}
        return {}

    def content_generation(self, state: BlogState) -> dict:
        """Generate blog content."""
        if state.topic:
            system_prompt = """You are expert blog writer. Use Markdown formatting.
                            Generate a detailed blog content with detailed breakdown for the {topic}"""
            system_message = system_prompt.format(topic=state.topic)
            response = self.llm.invoke(system_message)
            return {"blog": {"title": state.blog.title, "content": response.content}}
        return {}

    def translation(self, state: BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        Return ONLY the translated content, nothing else.
        Maintain the original formatting and style.

        Content to translate:
        {blog_content}
        """

        try:
            messages = [
                HumanMessage(
                    translation_prompt.format(
                        current_language=state.current_language,
                        blog_content=state.blog.content
                    )
                )
            ]

            # First try structured output
            try:
                translation_content = self.llm.with_structured_output(
                    Blog).invoke(messages)
                return {"blog": {"content": translation_content.content}}
            except Exception:
                # Fallback to regular completion if structured output fails
                response = self.llm.invoke(messages)
                return {"blog": {"content": response.content}}

        except Exception as e:
            print(f"Translation failed: {e}")
            return {"blog": {"content": f"Translation failed: {str(e)}"}}

    def route(self, state: BlogState) -> dict:
        """Prepare routing information."""
        return {"current_language": state.current_language}

    def route_decision(self, state: BlogState) -> str:
        """Route the content to the respective translation function."""
        language = state.current_language.lower()
        
        # Map all possible return values including English
        language_map = {
            "hindi": "hindi_translation",
            "french": "french_translation", 
            "urdu": "urdu_translation",
            "pashto": "pashto_translation",
            "german": "german_translation",
            "arabic": "arabic_translation",
            "russian": "russian_translation",
            "english": "__end__"  # Special key for English
        }
        
        return language_map.get(language, "__end__")  # Default to end for unknown languages

    # def route_decision(self, state: BlogState) -> str:
    #     """Determine translation route based on language."""
    #     language_map = {
    #         "hindi": "hindi",
    #         "french": "french",
    #         "urdu": "urdu",
    #         "pashto": "pashto",
    #         "german": "german",
    #         "arabic": "arabic",
    #         "russian": "russian"
    #     }
    #     return language_map.get(state.current_language.lower(), "english")
