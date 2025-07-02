from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext

from .prompts import root_instructions
from .tools import retrieve_rag_context

import os
from dotenv import load_dotenv
load_dotenv()

root_agent = Agent(
    model=os.getenv("ROOT_AGENT_MODEL"),
    name="decompose_agent",
    instruction=root_instructions(),
    tools=[
        retrieve_rag_context
    ]
)