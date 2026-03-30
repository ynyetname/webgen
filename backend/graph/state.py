from __future__ import annotations
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class GraphState(TypedDict):
    prompt: str
    template_type: str
    system_prompt: str
    messages: Annotated[list, add_messages]
    raw_response: str
    steps: list[dict]
    errors: list[str]