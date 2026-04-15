from typing import TypedDict, Optional

class AgentState(TypedDict):
    ticket: str
    category: Optional[str]
    confidence: Optional[float]
    context: Optional[str]
    context_score: Optional[float]
    decision: Optional[str]
    response: Optional[str]