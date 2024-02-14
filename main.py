from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas
from typing import List


Base.metadata.create_all(engine)  


app = FastAPI()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.post("/articles", response_model=schemas.Article, status_code=status.HTTP_201_CREATED)
def create_article(article: schemas.ArticleCreate, session: Session = Depends(get_session)):
    article_db = models.Article(**article.dict())
    session.add(article_db)
    session.commit()
    session.refresh(article_db)
    return article_db

@app.get("/articles/{id}", response_model=schemas.Article)
def read_article(id: int, session: Session = Depends(get_session)):
    article = session.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail=f"L'article {id} est introuvable")
    return article

@app.put("/articles/{id}", response_model=schemas.Article)
def update_article(id: int, article: schemas.ArticleCreate, session: Session = Depends(get_session)):
    article_db = session.query(models.Article).filter(models.Article.id == id).first()
    if not article_db:
        raise HTTPException(status_code=404, detail=f"L'article {id} est introuvable")
    for var, value in vars(article).items():
        setattr(article_db, var, value)
    session.commit()
    return article_db

@app.delete("/articles/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_article(id: int, session: Session = Depends(get_session)):
    article = session.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail=f"L'article {id} est introuvable")
    session.delete(article)
    session.commit()

@app.get("/articles", response_model=List[schemas.Article])
def read_articles(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    articles = session.query(models.Article).offset(skip).limit(limit).all()
    return articles
