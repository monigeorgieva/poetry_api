from pydantic import BaseModel
from typing import List


class ApiPoemByAuthorResponse(BaseModel):
    title: str
    author: str
    lines: List[str]
    linecount: int

