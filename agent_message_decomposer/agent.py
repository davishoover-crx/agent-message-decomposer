from google.adk.agents import LlmAgent

from .prompts import root_instructions
from .tools import retreive_data_with_vertex_ai_rag

import os
from dotenv import load_dotenv
load_dotenv()

root_agent = LlmAgent(
    model=os.getenv("ROOT_AGENT_MODEL"),
    name="decompose_agent",
    instruction=root_instructions(),
    tools=[
        retreive_data_with_vertex_ai_rag
    ]
)