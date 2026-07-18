from dataclasses import dataclass


@dataclass(slots=True)
class ToolCall:
    tool: str
    action: str
