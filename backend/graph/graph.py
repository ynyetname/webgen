from langgraph.graph import StateGraph, START, END
from .state import GraphState
from .nodes import detect_template, build_system_prompt, generate_code, parse_steps

def build_graph():
    g = StateGraph(GraphState)
    
    g.add_node("detect_template", detect_template)
    g.add_node("build_system_prompt", build_system_prompt)
    g.add_node("generate_code", generate_code)
    g.add_node("parse_steps", parse_steps)

    g.set_entry_point("detect_template")
    g.add_edge("detect_template", "build_system_prompt")
    g.add_edge("build_system_prompt", "generate_code")
    g.add_edge("generate_code", "parse_steps")
    g.add_edge("parse_steps", END)

    return g.compile()

graph = build_graph()