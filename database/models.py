
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, String, Integer
# from sqlalchemy.dialects.postgresql import UUID

from database.connection import Base, engine
from sqlalchemy.orm import declarative_base, mapped_column, Session

class SentenceEmbedding(Base):
    __tablename__ = "sentence_embeddings"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    embedding = embedding = mapped_column(Vector(384))

Base.metadata.create_all(engine)
