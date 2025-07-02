from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from vertexai.preview import rag

def retrieve_rag_context(rag_corpus_id: str):
    
    return VertexAiRagRetrieval(
        name="retrieve_rag_documentation",
        description=(
            """
                Use this tool to retrieve documentation and reference material for the request form the RAG corpus.
            """
        ),
        rag_resources=[
            rag.RagResource(
                rag_corpus=rag_corpus_id
            )
        ],
        similarity_top_k=10,
        vector_distance_threshold=0.6
    )