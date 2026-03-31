from fastapi import APIRouter
from langchain_core.messages import SystemMessage, HumanMessage
from schemas import TemplateRequest, TemplateResponse
from services.llm import llm_fast
from base_prompt import Base_prompt
from react_template import React_base_prompt
from node_template import Node_base_prompt

router = APIRouter()

@router.post("/template", response_model=TemplateResponse)
async def get_template(request: TemplateRequest):
    response = llm_fast.invoke([
        SystemMessage(content="Reply with ONLY 'react' or 'node'. Nothing else."),
        HumanMessage(content=request.prompt),
    ])
    template_type = response.content.strip().lower()
    if template_type == "node":
        template = Node_base_prompt
    else:
        template = React_base_prompt

    return TemplateResponse(
        prompts=[template],
        uiPrompts=[Base_prompt],
    )