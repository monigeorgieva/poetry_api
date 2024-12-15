from pydantic import BaseModel
from typing import List


class ApiAllAuthorsResponse(BaseModel):
   authors: List[str]
