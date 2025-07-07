from google.adk.agents.invocation_context import InvocationContext

def before_agent(callback_context: InvocationContext, rag_corpus_id: str):

    if "rag_corpus_id" not in callback_context.state:
        callback_context.state["rag_corpus_id"] = rag_corpus_id