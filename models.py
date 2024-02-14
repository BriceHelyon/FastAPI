from sqlalchemy import Column, Integer, String, DateTime
from database import Base

# Définit la classe Article à partir de Base
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    content = Column(String)
    publication_date = Column(DateTime)

    # def __repr__(self):
    #     return f"<Article(id={self.id}, title={self.title}, publication_date={self.publication_date})>"
