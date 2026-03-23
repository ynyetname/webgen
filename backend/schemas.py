from __future__ import annotations

from typing import Optional
from pydantic import BaseModel
from enum import Enum

class StepType(str, Enum):
    CreateFile = "CreateFile"
    CreateFolder = "CreateFolder"
    EditFile = "EditFile"
    DeleteFile = "DeleteFile"
    RunScript = "RunScript"

class Step(BaseModel):
    id: int
    title: str
    description: str = ""
    type: StepType
    status: str = "pending"
    code: Optional[str] = None
    path: Optional[str] = None

class FileItem(BaseModel):
    name: str
    type: str
    children: Optional[list[FileItem]] = None
    content: Optional[str] = None
    path: str

class TemplateRequest(BaseModel):
    prompt: str

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[ChatMessage]

class TemplateResponse(BaseModel):
    prompts: list[str]
    uiPrompts: list[str]

class ChatResponse(BaseModel):
    response: str

class BuildRequest(BaseModel):
    prompt: str

class BuildResponse(BaseModel):
    steps: list[Step]
    response: str
    template_type: str