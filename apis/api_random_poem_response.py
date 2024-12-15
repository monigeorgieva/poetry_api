from pydantic import BaseModel
from typing import List


class ApiRandomPoemResponse(BaseModel):
    title: str
    author: str
    lines: List[str]
    linecount: int
