from pydantic import BaseModel
from datetime import datetime


class ArticleCreate(BaseModel):
    title: str
    content: str
    publication_date: datetime


class Article(BaseModel):
    id: int
    title: str
    content: str
    publication_date: datetime

    class Config:
        orm_mode = True
