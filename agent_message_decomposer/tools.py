from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai import rag
from google.adk.tools import ToolContext

async def retreive_data_with_vertex_ai_rag(
        query: str,
        rag_corpora: str,
        similarity_top_k: int = 10,
        vector_distance_threshold: float = .6,
        tool_context: ToolContext = None
) -> list[str]:
    
    """
    Retrieves data using Vertex AI RAG.

    Args:
        query: The query text to retrieve data for.
        rag_corpora: A list of RAG corpora to use for retrieval.
        rag_resources: A list of RAG resources to use for retrieval.
        similarity_top_k: The top K similar results to return.
        vector_distance_threshold: The vector distance threshold for similarity.
        tool_context: The tool context for the operation.

    Returns:
        A list of retrieved text contexts or a message indicating no results.
    """

    if tool_context is None:
        tool_context = ToolContext()

    retrieval_tool = VertexAiRagRetrieval(
        name="vertex_ai_rag_retriever",
        description= "A tool for retrieving information using Vertex AI RAG.",
        rag_resources=[
            rag.RagResource(
                rag_corpus=rag_corpora
            )
        ],
        similarity_top_k=similarity_top_k,
        vector_distance_threshold=vector_distance_threshold
    )

    args = {"query": query}

    results = await retrieval_tool.run_async(args=args, tool_context=tool_context)

    if not isinstance(results, list):
        return []
    return results