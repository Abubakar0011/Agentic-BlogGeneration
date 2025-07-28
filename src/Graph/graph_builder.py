from langgraph.graph import StateGraph, START, END
from src.States.blogstate import BlogState
from src.LLM.Groq import GroqLLM
from src.Nodes.blog_nodes import BlogNode


# Graph Builder
class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)
        self.blog_node = BlogNode(llm)

    def build_graph(self, with_translations: bool = False):
        """Build the graph with or without translation nodes."""
        # Common nodes
        self.graph.add_node("title_creation", self.blog_node.title_creation)
        self.graph.add_node("content_generation", self.blog_node.content_generation)
        
        # Base workflow
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")

        if with_translations:
            self._add_translation_nodes()
            self.graph.add_edge("content_generation", "route")
            self.graph.add_conditional_edges(
                "route",
                self.blog_node.route_decision,
                {lang: f"{lang}_translation" for lang in [
                    "hindi", "french", "urdu", "pashto", "german", "arabic", "russian"
                ]}
            )
            for lang in ["hindi", "french", "urdu", "pashto", "german", "arabic", "russian"]:
                self.graph.add_edge(f"{lang}_translation", END)
        else:
            self.graph.add_edge("content_generation", END)

        return self.graph.compile()

    def _add_translation_nodes(self):
        """Add translation nodes to the graph."""
        self.graph.add_node("route", self.blog_node.route)
        translations = [
            ("hindi", "hindi"),
            ("french", "french"),
            ("urdu", "urdu"),
            ("pashto", "pashto"),
            ("german", "german"),
            ("arabic", "arabic"),
            ("russian", "russian")
        ]
        
        for lang_key, lang_value in translations:
            self.graph.add_node(
                f"{lang_key}_translation",
                lambda state, lang=lang_value: self.blog_node.translation(
                    BlogState(
                        topic=state.topic,
                        blog=state.blog,
                        current_language=lang
                    )
                )
            )


# Below code is for the langsmith langgraph studio
llm = GroqLLM().get_llm()

# get the graph
graph_builder = GraphBuilder(llm)
graph = graph_builder.build_graph(with_translations=True)
