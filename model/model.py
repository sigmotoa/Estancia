from pydantic import BaseModel, HttpUrl, Field
from typing import List, Dict, Any, Optional

class CourseContent(BaseModel):
    topic:str
    description:Optional[str]=None
    resources:Optional[List[HttpUrl]]=None

class CourseItem(BaseModel):
    id:int
    title:str
    key_contents: List[CourseContent]
