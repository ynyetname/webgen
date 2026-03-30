from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
from langchain_core.messages import HumanMessage
from schemas import ChatRequest
from graph.graph import graph
import json

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    lc_messages = [
        HumanMessage(content=m.content)
        for m in request.messages
        if m.role == "user"
    ]

    async def event_stream():
        async for chunk in graph.astream({
            "prompt": lc_messages[-1].content if lc_messages else "",
            "messages": lc_messages,
            "template_type": "",
            "system_prompt": "",
            "raw_response": "",
            "steps": [],
            "errors": [],
        }):
            for node_name, node_output in chunk.items():
                yield {
                    "event": "node_update",
                    "data": json.dumps({
                        "node": node_name,
                        "output": node_output,
                    }),
                }
        yield {"event": "done", "data": "{}"}

    return EventSourceResponse(event_stream())