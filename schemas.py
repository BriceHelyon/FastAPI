from pydantic import BaseModel
from datetime import datetime

# Crée le schéma ArticleCreate (Modèle Pydantic)
class ArticleCreate(BaseModel):
    title: str
    content: str
    publication_date: datetime

# Complète le schéma Article (Modèle Pydantic)
class Article(BaseModel):
    id: int
    title: str
    content: str
    publication_date: datetime

    class Config:
        orm_mode = True
