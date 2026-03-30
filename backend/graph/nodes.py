from __future__ import annotations
from langchain_core.messages import SystemMessage, HumanMessage
from services.llm import llm, llm_chat
from system_prompt import get_system_prompt
from base_prompt import Base_prompt
from react_template import React_base_prompt
from node_template import Node_base_prompt
from .state import GraphState
import re

def detect_template(state: GraphState) -> str:
    
    response = llm_chat([
        SystemMessage(content="Reply with only 'react' or 'node', nothing else.")],
        HumanMessage(content=state["prompt"])
    )
    
    template_type = response.content.strip().lower()
    if template_type not in ("react", "node"):
        template_type = "react"
    return {"template_type": template_type}


def build_system_prompt(state: GraphState) -> dict:
    template = (
        React_base_prompt if state["template_type"] == "react"
        else Node_base_prompt   
    )
    
    full_system_prompt = Base_prompt + "\n\n" + get_system_prompt() + "\n\n" + template
    
    return {"system_prompt": full_system_prompt}

def generate_code(state: GraphState) -> dict:
    messages = [
        SystemMessage(content=state["system_prompt"]),
        *state["messages"],
    ]
    response = llm.invoke(messages)
    return {
        "raw_response": response.content,
        "messages": [response],
    }
    
def parse_steps(state: GraphState) -> dict:
    raw = state["raw_response"]
    steps = []
    step_id = 1

    file_pattern = re.compile(
        r'<boltAction\s+type="file"\s+filePath="([^"]+)">(.*?)</boltAction>',
        re.DOTALL,
    )
    
    for match in file_pattern.finditer(raw):
        file_path, content = match.group(1), match.group(2).strip()
        steps.append({
            "id": step_id,
            "title": f"Create {file_path}",
            "type": "CreateFile",
            "status": "done",
            "code": content,
            "path": file_path,
        })
        step_id += 1
        
        shell_pattern = re.compile(
        r'<boltAction\s+type="shell">(.*?)</boltAction>',
        re.DOTALL,
    )
    for match in shell_pattern.finditer(raw):
        command = match.group(1).strip()
        steps.append({
            "id": step_id,
            "title": f"Run: {command[:60]}",
            "type": "RunScript",
            "status": "done",
            "code": command,
        })
        step_id += 1
        
    return {"steps": steps, "errors": []}

